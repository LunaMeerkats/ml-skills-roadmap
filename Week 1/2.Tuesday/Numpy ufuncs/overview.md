## 1. **Arithmetic ufuncs**

Work element-wise on arrays.

* `np.add`, `np.subtract`, `np.multiply`, `np.divide`, `np.floor_divide`
* `np.negative`, `np.power`, `np.mod`

---

## 2. **Comparison ufuncs**

Return Boolean arrays for element-wise comparisons.

* `np.equal`, `np.not_equal`
* `np.less`, `np.less_equal`
* `np.greater`, `np.greater_equal`

---

## 3. **Logical ufuncs**

Operate on Boolean arrays.

* `np.logical_and`, `np.logical_or`, `np.logical_xor`, `np.logical_not`

---

## 4. **Trigonometric ufuncs**

For radians-based math.

* `np.sin`, `np.cos`, `np.tan`
* `np.arcsin`, `np.arccos`, `np.arctan`
* `np.arctan2` (safe for x,y quadrants)

---

## 5. **Exponential & logarithmic ufuncs**

Common in statistics, ML, and transforms.

* `np.exp`, `np.expm1` (better for small values)
* `np.log`, `np.log10`, `np.log2`, `np.log1p` (better for small values)

---

## 6. **Rounding ufuncs**

For control over numerical precision.

* `np.round`, `np.floor`, `np.ceil`, `np.trunc`

---

## 7. **Aggregate-style ufuncs (axis-aware)**

While not technically ufuncs in the strictest sense, they often wrap them for reductions.

* `np.sum`, `np.prod`
* `np.min`, `np.max`
* `np.mean`, `np.std`, `np.var`

---

## 8. **Special useful ones**

* `np.abs` / `np.fabs` (fabs ignores complex numbers)
* `np.clip` (bounds values between min and max)
* `np.sign`
* `np.sqrt`
* `np.cbrt`
* `np.hypot` (distance from origin)
* `np.deg2rad`, `np.rad2deg`

---

If you know all of these, you can:

* Replace most Python `for` loops with **vectorized** operations.
* Keep your code cleaner and significantly faster.
* Work consistently with broadcasting, masking, and aggregation.
