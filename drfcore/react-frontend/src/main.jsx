import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import { HashRouter } from "react-router-dom";
import "./App.css";
import CustomThemeProvider from "./theme/CustomThemeProvider.jsx";
import { DataProvider } from "./DataContext.jsx";
ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <DataProvider>
      <CustomThemeProvider>
        <HashRouter>
          <App />
        </HashRouter>
      </CustomThemeProvider>
    </DataProvider>
  </React.StrictMode>
);
