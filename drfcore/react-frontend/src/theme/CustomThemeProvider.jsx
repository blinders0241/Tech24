import React, { useState, useMemo, createContext } from "react";
import { ThemeProvider, createTheme } from "@mui/material";
import { darkTheme, lightTheme } from "./theme";

export const ColorModeContext = createContext({ toggleColorMode: () => {} });

export default function CustomThemeProvider(props) {
  const { children } = props;
  const [mode, setMode] = useState("light");
  const colorMode = useMemo(
    () => ({
      toggleColorMode: () => {
        setMode((prevMode) => (prevMode === "light" ? "dark" : "light"));
      },
    }),
    []
  );

  const theme = useMemo(() => {
    if (mode === "light") {
      return createTheme(lightTheme);
    }
    return createTheme(darkTheme);
  }, [mode]);
  console.log(mode);
  return (
    <ColorModeContext.Provider value={colorMode}>
      <ThemeProvider theme={theme}>{children}</ThemeProvider>
    </ColorModeContext.Provider>
  );
}
