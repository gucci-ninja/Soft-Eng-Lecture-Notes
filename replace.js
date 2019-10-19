const lookup = {
  // Greek
  alpha: "α",
  beta: "β",
  gamma: "γ",
  delta: "δ",
  epsilon: "ε",
  zeta: "ζ",
  eta: "η",
  theta: "θ",
  iota: "ι",
  kappa: "κ",
  lambda: "λ",
  mu: "μ",
  nu: "ν",
  xi: "ξ",
  omicron: "ο",
  pi: "π",
  rho: "ρ",
  sigma: "σ",
  ssigma: "ς",
  tau: "τ",
  upsilon: "υ",
  phi: "φ",
  chi: "χ",
  psi: "ψ",
  omega: "ω",

  // Math
  // "+-": "±",
  // "*": "×",
  // "/": "÷",
  sqrt: "√",
  integral: "∫",
  inf: "∞",
  "/=": "≠",
  approx: "≈",
  equiv: "≡",
  prop: "∝",
  ">=": "≥",
  "<=": "≤",

  // Set theory
  elem: "∈",
  nelem: "∉",
  natN: "ℕ",
  intZ: "ℤ",
  ratio: "ℚ",
  realR: "ℝ",
  aleph: "ℵ",
  concat: "◦",

  // ⊆ ⊇

  // Logic
  not: "¬",
  "∝": "prop",
  forall: "∀",

  // Arrows
  "<=>": "⇔",
  "=>": "⇒",

  // Subscripts
  _0: "₀",
  _1: "₁",
  _2: "₂",
  _3: "₃",
  _4: "₄",
  _5: "₅",
  _6: "₆",
  _7: "₇",
  _8: "₈",
  _9: "₉",

  // Superscripts
  "^0": "⁰",
  "^1": "¹",
  "^2": "²",
  "^3": "³",
  "^4": "⁴",
  "^5": "⁵",
  "^6": "⁶",
  "^7": "⁷",
  "^8": "⁸",
  "^9": "⁹",

  // Geometry

  // Arabic, Hebrew

  // Cultural
  man: "♂",
  woman: "♀"

  // Music
};

function replace(file) {
  const fs = require('fs');
  var data = fs.readFileSync(file, "utf8");
  var res = data;
  for (var key in lookup) {
    res = res.replace(new RegExp('//'+key, 'g'), lookup[key]);
  }
  
  console.log(res);
  fs.writeFile('test.md', res, 'utf8', (err) => {
    if (err) throw err;
});
}

replace(process.argv[2]);