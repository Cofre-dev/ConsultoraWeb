// postcss.config.cjs
const autoprefixer = require("autoprefixer");
const tailwindcss = require("tailwindcss"); // O el paquete que estés usando

module.exports = {
  plugins: {
    '@tailwindcss/postcss': {},
    // tailwindcss: {},
    autoprefixer: {},
  },
};