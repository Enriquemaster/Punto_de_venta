/** @type {import('tailwindcss').Config} */
module.exports = {

  plugins: [],

  content: [
    './templates/**/*.html', // Escanear todos los archivos HTML en el directorio templates
    './static/styles/**/*.css', // Escanear archivos CSS si estás usando clases en CSS
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

