# rust_neural_compression
## Planning
I plan to make this neural compression using rust to compress and decompress information sent over uart between two raspberry pis.
I will use chatgpt-5 to help plan this.

## Plan
### Goals & Scope

* **Purpose:** Neural **lossless** compressor for arbitrary byte streams sent over **UART between two Raspberry Pis**.
* **MVP:** File/pipe compressor (`.ncmp`) + **streaming mode** for UART with framing and CRC.
* **Model:** Tiny byte-level neural probability model (autoregressive) + **rANS** entropy coding.
* **Targets:**

  * Decode ≥ **8 MB/s** on Pi 4/5; Encode ≥ **2 MB/s** with the tiny model.
  * Compression better than `zlib -6` on JSON/log/code corpora (stretch goal).

---

### Architecture

```
[trainer (PyTorch)] → [weights.bin + meta.json]
        │
        ▼
[codec-core (Rust, rANS + bitstream)]
   ├─ model-byte (Rust: int8 inference, autoregressive PMF)
   ├─ cli (encode/decode, corpus tests, benches)
   └─ stream-uart (UART framing, CRC, flow control)
```

---

### Milestones (Sprints)

#### Sprint 1 — Plumbing & rANS

* [ ] **Bitstream container** with header, chunks, CRC32 (see spec below).
* [ ] **rANS** encoder/decoder (12–15-bit CDF precision, normalized).
* [ ] CLI: `ncmp encode in > out.ncmp`, `ncmp decode out.ncmp > recon`.
* [ ] Tests: round-trip, fuzz bitstream, property tests for rANS.

#### Sprint 2 — Minimal Neural PMF (CPU-friendly)

* [ ] PyTorch trainer: tiny **GRU(256)×2** or **causal conv (Wavenet-lite)** for bytes.
* [ ] Export **int8 weights** + per-layer scale/zero-point (`weights.bin`, `meta.json`).
* [ ] Rust **int8 inference**: only ops you need (embedding/conv1d or GRU cell, affine, ReLU).
* [ ] Parity tests vs. Python on fixed inputs.
* [ ] Replace uniform PMF with **neural PMF** in encoder/decoder.

#### Sprint 3 — Streaming over UART

* [ ] `stream-uart`: framing (**SLIP** or **COBS**), **CRC32**, simple **ACK/seq** (stop-and-wait).
* [ ] Chunked coding: 64–256 KiB blocks → framed packets (MTU \~1–4 KiB).
* [ ] Tools: `ncmp tx /dev/ttyUSB0 < file`, `ncmp rx /dev/ttyUSB1 > file`.
* [ ] Soak tests: loopback + error injection (drop/flip bytes).

#### Sprint 4 — Performance & Quality

* [ ] Benchmarks on Pi 4/5: tokens/s, MB/s, memory footprint.
* [ ] Model size sweeps (d=128/256, 1–2 layers).
* [ ] Compare vs. `gzip`, `zstd -1..-3` on representative corpora.
* [ ] Optional: SIMD (NEON) feature flag for inference hot paths.

#### Sprint 5 — Hardening

* [ ] Bit-exact determinism across builds.
* [ ] Corpus of golden files; CI runs encode→decode→CRC check.
* [ ] CLI UX polish + docs + examples.

---

### Repository / Crate Layout

```
rust_neural_compression/
  Cargo.toml
  crates/
    codec-core/      # rANS, bitstream, CRC, chunking
    model-byte/      # int8 runtime + neural PMF for bytes
    stream-uart/     # SLIP/COBS framing, ACK/seq, serial I/O
    cli/             # ncmp {encode,decode,tx,rx,bench}
  training/
    byte_model.ipynb # trainer + export
  tools/
    export_weights.py
    corpus/          # sample data & test lists
```

---

### Bitstream Container (File Mode)

**Header (LE, fixed size):**

```
magic:   u32 = 0x004D434E      // "NCM\0"
ver:     u16 = 0x0001
model_id:u16                   // hash of meta.json
flags:   u32                   // bits: 0=file,1=stream-origin, etc.
orig_len:u64                   // bytes before compression
chunk_sz:u32                   // suggested decode block (e.g., 131072)
meta_ofs:u32                   // 0 if none (weights referenced externally)
data_ofs:u32                   // first chunk offset
hdr_crc: u32
```

**Chunk format (repeated):**

```
chunk_len:u32   // compressed bytes following
raw_len:  u32   // uncompressed bytes this chunk
cdf_tag:  u16   // model snapshot / table id
reserved: u16
payload:  [u8; chunk_len]
chunk_crc:u32
```

---

### UART Wire Protocol (Streaming Mode)

* **Framing:** **COBS** (byte-stuffing, 0x00 as packet delimiter) or **SLIP** (simpler, slightly more overhead).
* **Packet:**

  ```
  kind: u8   // 0x01=DATA, 0x02=ACK, 0x03=MODEL, 0x04=PING
  seq:  u16  // modulo 4096
  len:  u16  // payload length
  body: [u8; len] // may hold partial or whole compressed chunk
  crc32:u32
  ```
* **Flow control:** stop-and-wait (one in flight) for MVP; upgrade to window=4 later.
* **Model sync:** sender transmits MODEL packet once per session if receiver model\_id mismatch.

---

### Model & Training (byte-level, lossless)

* **Tokenization:** raw bytes `[0..255]`.
* **Model (pick one):**

  * **GRU 256×2** → affine → logits(256); or
  * **Causal Conv1D**: 4–6 layers, k=3, d=128–256, gated or ReLU.
* **Loss:** cross-entropy; teacher forcing.
* **Quantization-aware training:** int8 weights; int16 accumulators in Rust.
* **Export:** flat `weights.bin` + `meta.json` (layer order, shapes, scales).
* **Inference contract:** given context window `x[ t-k .. t-1 ]`, return **CDF\[256]** (Q=12..15 bits).

---

### CLI (initial)

```bash
# File mode
ncmp encode path/to/input > out.ncmp
ncmp decode out.ncmp > recon

# Streaming (two Pis, /dev/serialX vary)
ncmp tx --port /dev/ttyUSB0 < input.bin
ncmp rx --port /dev/ttyUSB1 > output.bin

# Benches
ncmp bench --corpus tools/corpus --model models/byte-tiny
```

---

### Testing & Validation

* **Round-trip**: bit-exact equality for files and stream.
* **Fuzz**: bitstream parser, rANS symbol loops, COBS/SLIP decoder.
* **Error injection**: flip/drop bytes on stream; ensure desync recovery (next packet boundary) and clear error codes.
* **Parity**: inference layer-by-layer vs. Python with fixed seeds.
* **Metrics**: bpb, ratio, MB/s encode/decode, RAM high-water mark.

---

### Performance Targets & Flags

* **Targets:** Pi 4/5 aarch64, Rust stable.
* **Features:** `simd` (NEON), `fast-math` (encoder only), `tiny-model` (GRU×1).
* **Memory:** ≤ 32 MB resident (MVP far below).

---

### Risks & Mitigations

* **Neural encode cost:** keep models tiny; consider **look-back window** (k=256–1024) and cache states.
* **UART errors:** use CRC + ACK; small MTU to localize loss.
* **Drift between models:** enforce `model_id` handshake; refuse to decode mismatch.

---

### Next Steps (today)

1. Scaffold workspace & crates (`codec-core`, `cli`).
2. Implement **rANS** + uniform PMF; pass round-trip & fuzz.
3. Add **COBS** framing + CRC32; loopback test on a single Pi.
4. Train **GRU(256)×1** toy model; export; wire into encoder/decoder.
5. Run corpus compare vs. `gzip -6` and `zstd -1`; record results in README.
