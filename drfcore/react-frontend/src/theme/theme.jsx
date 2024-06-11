// import AmadeusFont from '../assets/fonts/Amadeus-Light.ttf';

// const amadeus = {
//   fontFamily: 'Amadeus',
//   fontStyle: 'light',
//   fontDisplay: 'swap',
//   fontWeight: 400,
//   src: `
//     local('Amadeus'),
//     local('Amadeus-Light'),
//     url(${AmadeusFont}) format('ttf')
//   `,
// }

const commonTypography = {
  fontFamily: '"Amadeus", "Source Sans Pro"',
  h1: {
    fontWeight: "300",
  },
};

export const darkTheme = {
  palette: {
    type: "dark",
    primary: {
      main: "#536DFE",
      light: "#3F51B5",
      contrastText: "#fff",
    },
    secondary: {
      main: "#FF5252",
    },
    success: {
      main: "#7cb342",
    },
    warning: {
      main: "#fdd835",
    },
    error: {
      main: "#e53935",
    },
    info: {
      main: "#00A9E0",
    },
    text: {
      primary: "#ffffff",
    },
    background: {
      default: "#363636",
      paper: "#212121",
    },
    divider: "#bdbdbd",
  },
  //   typography: commonTypography,
  //   overrides: {
  //     MuiCssBaseline: {
  //       "@global": {
  //         "@font-face": [amadeus],
  //       },
  //     },
  //   },
};

export const lightTheme = {
  palette: {
    type: "light",
    primary: {
      main: "#1565C0",
      light: "#F6F6F6",
      contrastText: "#000",
    },
    secondary: {
      main: "#FF8A80",
    },
    success: {
      main: "#00e676",
    },
    warning: {
      main: "#b84300",
    },
    error: {
      main: "#f44336",
    },
    info: {
      main: "#0025cc",
    },
    background: {
      default: "#fafafa",
      paper: "#9BCAEB",
    },
    divider: "#757575",
  },
  //   typography: commonTypography,
  //   overrides: {
  //     MuiCssBaseline: {
  //       "@global": {
  //         "@font-face": [amadeus],
  //       },
  //     },
  //   },
};
