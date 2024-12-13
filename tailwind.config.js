/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", // Asegúrate de que Tailwind escanee tus archivos HTML
    "./static/js/**/*.js",    // Si tienes archivos JavaScript que usan Tailwind
  ],
  theme: {
    extend: {
      // Aquí puedes agregar tus personalizaciones de tema
      fontFamily: {
        sans: ['Poppins', 'sans-serif'], // Establece Poppins como la fuente sans por defecto
      },
      colors: {
        'color-primario': '#082f49', // Ejemplo de color personalizado
        'color-secundario': '#374151',
        'color-tres': '#a3a3a3',
        'color-base': '#e5e5e5',
      },
      spacing: {
        '128': '32rem', // Ejemplo de espaciado personalizado
      },
    },
  },
  plugins: [],
}
