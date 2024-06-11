import React, { useState } from "react";
import { AgGridReact } from "ag-grid-react";
import "ag-grid-community/styles/ag-grid.css";
import "ag-grid-community/styles/ag-theme-alpine.css";

const DataGrid2 = ({ data2, columnDefs }) => {
  // console.log(data2);
  const [gridApi, setGridApi] = useState(null);
  const onGridReady = (params) => {
    setGridApi(params.api);
    params.columnApi.applyColumnState({
      state: [{ colId: "id", sort: "desc" }],
      defaultState: { sort: null },
    });
  };
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
        rowData={data2}
        pagination={true}
        // getRowStyle={getRowStyle}
        rowClassRules={rowClassRules}
      />
    </div>
  );
};

export default DataGrid2;
