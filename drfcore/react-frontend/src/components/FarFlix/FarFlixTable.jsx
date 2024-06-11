import React, { useEffect, useState } from "react";
import { AgGridReact } from "ag-grid-react";
import { Routes, Route, useNavigate } from "react-router-dom";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import "ag-grid-community/styles/ag-grid.css";
import "ag-grid-community/styles/ag-theme-alpine.css";
import "ag-grid-enterprise";
import FarFlixMovieDetailsPage from "./FarFlixMovieDetailsPage";

const FarFlixTable = ({ rowData, columnDefs }) => {
  const detailRowAutoHeight = true;
  const [gridApi, setGridApi] = useState(null);
  const [gridColumnApi, setGridColumnApi] = useState(null);
  const [trigger, setTrigger] = useState(0);
  const onGridReady = (params) => {
    setGridApi(params.api);
    setGridColumnApi(params.columnApi);
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
        let selectedValue = selectedRows[0].Title_IMDB;
        console.log(selectedValue);
        gridApi.getFilterInstance("Title_IMDB").setModel({
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
          // className="ag-theme-balham"
          style={{
            height: "888px",
            width: "1400px",
          }}
        >
          <AgGridReact
            detailRowAutoHeight={detailRowAutoHeight}
            onGridReady={onGridReady}
            columnDefs={columnDefs}
            rowData={rowData}
            pagination={true}
            rowSelection="single" // Enable multiple row selection
            onSelectionChanged={onSelectionChanged}
            onCellDoubleClicked={onCellDoubleClicked}
            masterDetail={true}
            detailCellRenderer={(props) => (
              <FarFlixMovieDetailsPage {...props} />
            )}
            onFirstDataRendered={onFirstDataRendered}
          ></AgGridReact>
        </div>
      </Col>
    </Row>
  );
};

export default FarFlixTable;
