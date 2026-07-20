/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        ink: "#0E1116",
        surface: "#151A23",
        surfaceHi: "#1D2430",
        border: "#252C3A",
        amber: { DEFAULT: "#F0B429", dim: "#B98410" },
        teal: { DEFAULT: "#2DD4BF", dim: "#0F8F82" },
        mist: "#9AA5B8",
      },
      fontFamily: {
        display: ["\"Space Grotesk\"", "sans-serif"],
        body: ["\"Inter\"", "sans-serif"],
      },
    },
  },
  plugins: [],
};
