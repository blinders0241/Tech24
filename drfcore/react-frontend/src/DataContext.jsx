import React from "react";

// Create a context with default value as an empty array
export const DataContext = React.createContext([]);

export const DataProvider = ({ children }) => {
  const [data, setData] = React.useState([]);

  return (
    <DataContext.Provider value={[data, setData]}>
      {children}
    </DataContext.Provider>
  );
};
