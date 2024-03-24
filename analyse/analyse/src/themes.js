import { createTheme } from '@mui/material/styles';

const theme = createTheme({
  palette: {
    primary: {
      main: '#007bff', // Change la couleur principale du thème (couleur de base)
    },
    background: {
      default: '#E5EAF2', // Change la couleur de fond par défaut du site
    },
  },
});

export default theme;