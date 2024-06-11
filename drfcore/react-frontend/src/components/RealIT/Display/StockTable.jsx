import React, { useState } from "react";
import { AgGridReact } from "ag-grid-react";

import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import "ag-grid-community/styles/ag-grid.css";
import "ag-grid-community/styles/ag-theme-alpine.css";
import "ag-grid-enterprise";
import DetailsComponent from "./DetailsComponents";

const StockTable = ({ rowData, columnDefs }) => {
  // const gridRef = useRef();
  const [gridApi, setGridApi] = useState(null);
  const [gridColumnApi, setGridColumnApi] = useState(null);
  const [trigger, setTrigger] = useState(0);

  const onGridReady = (params) => {
    setGridApi(params.api);
    setGridColumnApi(params.columnApi);
    // Sort the data in descending order of dates on load
    params.columnApi.applyColumnState({
      state: [{ colId: "CHG_IN_OI", sort: "desc" }],
      defaultState: { sort: null },
    });
  };

  const onCellDoubleClicked = (params) => {
    navigator.clipboard.writeText(params.value);
    alert("Copied: " + params.value);
  };

  // Add gridApi as a dependency to the useEffect hook
  const onSelectionChanged = () => {
    if (gridApi) {
      // Check if gridApi is not null
      let selectedRows = gridApi.getSelectedRows();
      if (selectedRows.length > 0) {
        // Check if any row is selected
        let selectedValue = selectedRows[0].SYMBOL;
        console.log(selectedValue);
        gridApi.getFilterInstance("SYMBOL").setModel({
          type: "equals",
          filter: selectedValue,
        });

        // Apply the filter
        gridApi.onFilterChanged();
      }
    }
  };

  const onFirstDataRendered = (params) => {
    params.api.forEachNode((node) => {
      columnDefs.forEach((colDef) => {
        if (
          node.data[colDef.field] === undefined ||
          node.data[colDef.field] === null
        ) {
          params.columnApi.setColumnVisible(colDef.field, false);
        }
      });
    });
  };

  return (
    <Row>
      <Col>
        <div
          className="ag-theme-alpine-auto-dark"
          style={{
            height: "888px",
            width: "100%",
          }}
        >
          <AgGridReact
            onGridReady={onGridReady}
            columnDefs={columnDefs}
            rowData={rowData}
            pagination={true}
            domLayout={"autoHeight"}
            rowSelection="single" // Enable multiple row selection
            onSelectionChanged={onSelectionChanged}
            onCellDoubleClicked={onCellDoubleClicked}
            masterDetail={true}
            detailCellRenderer={(props) => <DetailsComponent {...props} />}
            onFirstDataRendered={onFirstDataRendered}
          ></AgGridReact>
        </div>
      </Col>
    </Row>
  );
};

export default StockTable;
