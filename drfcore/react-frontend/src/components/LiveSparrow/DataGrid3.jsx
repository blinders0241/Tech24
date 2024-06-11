import React, { useState } from "react";
import { AgGridReact } from "ag-grid-react";
import "ag-grid-community/styles/ag-grid.css";
import "ag-grid-community/styles/ag-theme-alpine.css";

const DataGrid3 = ({ data3, columnDefs }) => {
  const [gridApi, setGridApi] = useState(null);
  const onGridReady = (params) => {
    setGridApi(params.api);
    params.columnApi.applyColumnState({
      state: [{ colId: "id", sort: "desc" }],
      defaultState: { sort: null },
    });
  };
  // const getRowStyle = (params) => {
  //   if (flag) {
  //     // replace 'flag' with your actual flag field name
  //     return { backgroundColor: "yellow" }; // replace 'yellow' with your desired color
  //   }
  // };

  const rowClassRules = {
    "rag-green": "data.PCR >= 1.25",
    "rag-amber": "data.PCR >= 76 && data.PCR < 1.26",
    "rag-red": "data.PCR <= 0.75",
  };

  return (
    <div className="ag-theme-quartz" style={{ height: "310px", width: "100%" }}>
      <AgGridReact
        onGridReady={onGridReady}
        columnDefs={columnDefs}
        rowData={data3}
        pagination={true}
        // getRowStyle={getRowStyle}
        rowClassRules={rowClassRules}
      />
    </div>
  );
};

export default DataGrid3;
