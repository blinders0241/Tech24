import { AgGridReact } from "ag-grid-react";
import "ag-grid-community/styles/ag-grid.css";
import "ag-grid-community/styles/ag-theme-balham.css";

const MyGridComponent = ({ columnDefs, rowData }) => {
  return (
    <div
      className="ag-theme-quartz"
      style={{
        height: "990px",
        width: "100%",
      }}
    >
      <AgGridReact columnDefs={columnDefs} rowData={rowData}></AgGridReact>;
    </div>
  );
};
export default MyGridComponent;
