/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", // Asegúrate de que Tailwind escanee tus archivos HTML
    "./static/js/**/*.js",    // Si tienes archivos JavaScript que usan Tailwind
  ],
  theme: {
    extend: {
      // Aquí puedes agregar tus personalizaciones de tema
      colors: {
        'custom-color': '#1DA1F2', // Ejemplo de color personalizado
      },
      spacing: {
        '128': '32rem', // Ejemplo de espaciado personalizado
      },
    },
  },
  plugins: [],
}
