/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html"],
  safelist: [
    { pattern: /bg-(bg|surface|surface-2|primary|primary-dark|copper|copper-light|muted|muted-light|danger|text)/ },
    { pattern: /text-(bg|surface|primary|primary-dark|copper|copper-light|muted|muted-light|danger|text)/ },
    { pattern: /border-(bg|surface|primary|primary-dark|copper|copper-light|muted|muted-light|danger|text)/ },
    { pattern: /from-(bg|surface|primary|primary-dark|copper|copper-light|muted|muted-light|danger|text)/ },
    { pattern: /to-(bg|surface|primary|primary-dark|copper|copper-light|muted|muted-light|danger|text)/ },
    { pattern: /via-(bg|surface|primary|primary-dark|copper|copper-light|muted|muted-light|danger|text)/ },
    { pattern: /font-(bebas|inter)/ },
  ],
  theme: {
    extend: {
      colors: {
        bg:            '#0D1117',
        surface:       '#161B22',
        'surface-2':   '#1C2333',
        primary:       '#F97316',
        'primary-dark':'#EA6C0A',
        copper:        '#B45309',
        'copper-light':'#D97706',
        text:          '#F1F5F9',
        muted:         '#64748B',
        'muted-light': '#94A3B8',
        danger:        '#EF4444',
      },
      fontFamily: {
        bebas: ['"Bebas Neue"', 'sans-serif'],
        inter: ['Inter', 'sans-serif'],
      },
    }
  },
  plugins: [],
}
