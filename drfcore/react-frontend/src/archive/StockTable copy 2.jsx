import React, { useEffect, useState } from "react";
import { AgGridReact } from "ag-grid-react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import "ag-grid-community/styles/ag-grid.css";
import "ag-grid-community/styles/ag-theme-alpine.css";
import "ag-grid-enterprise";

//Components called in this
import DetailsComponent from "../components/DetailsComponents";

const allNotesapi = "http://127.0.0.1:8000/api/";

const StockTable = () => {
  const [gridApi, setGridApi] = useState(null);
  const [gridColumnApi, setGridColumnApi] = useState(null);
  const [rowData, setRowData] = useState([]);
  const columnDefs = [
    // { headerName: "ID", field: "id", width: 80 },
    //Symbol
    {
      headerName: "SYMBOL",
      field: "SYMBOL",
      width: 130,
      filter: "agTextColumnFilter",
      floatingFilter: true,
      cellRenderer: "agGroupCellRenderer",
      // flex: 1,
    },

    //OpenPrice
    // {
    //   headerName: "OPEN",
    //   field: "OPEN",
    //   width: 115,
    //   valueFormatter: (params) => {
    //     return "₹" + params.value.toLocaleString();
    //   },
    // },
    //HighPrice
    // {
    //   headerName: "HIGH",
    //   field: "HIGH",
    //   width: 110,
    //   valueFormatter: (params) => {
    //     return "₹" + params.value.toLocaleString();
    //   },
    // },
    // LowPrice
    {
      headerName: "LOW",
      field: "LOW",
      width: 110,
      valueFormatter: (params) => {
        return "₹" + params.value.toLocaleString();
      },
    },
    // ClosingPrice
    {
      headerName: "Close",
      field: "CLOSE",
      width: 110,
      valueFormatter: (params) => {
        return "₹" + params.value.toLocaleString();
      },
      // Volume
    },
    //Volume
    {
      headerName: "Volume",
      field: "VOLUME",
      width: 110,
      cellStyle: (params) =>
        params.value > 50000 ? { color: "green" } : { color: "red" },
    },
    { headerName: "OpenInterest", field: "OPEN_INT", width: 122 },
    {
      headerName: "OI_Change",
      field: "CHG_IN_OI",
      width: 110,
      // cellStyle: (params) => console.log(typeof params.value),
    },
    {
      headerName: "Timestamp",
      field: "TIMESTAMP",
      width: 150,
      filter: "agDateColumnFilter",
      valueGetter: (params) => {
        // console.log(params.data.TIMESTAMP);
        let receivedDate = params.data.TIMESTAMP.split(" ")[0];
        let dateParts = receivedDate.split("-");
        // console.log(dateParts);

        return new Date(dateParts[0], dateParts[1] - 1, dateParts[2]);
      },
      // valueFormatter: (params) => {
      //   return moment(params.value).format("ddd, DD-MMM-YY");
      // },
    },
  ];

  useEffect(() => {
    fetch(allNotesapi + "displayBhavcopy/") // replace 'your-api-url' with your API URL
      .then((result) => result.json())
      .then((rowData) => setRowData(rowData));
  }, []);

  const onGridReady = (params) => {
    // const [maxValue, setMaxValue] = useState(null);
    setGridApi(params.api);
    setGridColumnApi(params.columnApi);
    // Sort the data in descending order of dates on load
    params.columnApi.applyColumnState({
      state: [{ colId: "TIMESTAMP", sort: "desc" }],
      defaultState: { sort: null },
    });
  };
  const onSelectionChanged = () => {
    // console.log(gridApi.getSelectedRows());
    let selectedRows = gridApi.getSelectedRows();
    // console.log(selectedRows[0].SYMBOL);
    let selectedValue = selectedRows[0].SYMBOL;

    gridApi.getFilterInstance("SYMBOL").setModel({
      type: "equals",
      filter: selectedValue,
    });

    // Apply the filter
    gridApi.onFilterChanged();
  };

  const selectLatestDate = () => {
    let latestDate = "";
    // Find the latest date in the data
    gridApi.forEachNode((node) => {
      let nodeDate = new Date(node.data.TIMESTAMP);
      let nodeDateString = nodeDate.toISOString().split(" ")[0]; // convert to 'YYYY-MM-DD' format
      console.log("nodeDateString", nodeDateString);

      if (latestDate === "" || nodeDateString > latestDate) {
        latestDate = nodeDateString;
      }
    });
    console.log("latestDate", latestDate);
    // Set filter model for the column
    gridApi.getFilterInstance("TIMESTAMP").setModel({
      type: "equals",
      filter: latestDate,
    });
    // Apply the filter
    gridApi.onFilterChanged();
  };
  const onCellDoubleClicked = (params) => {
    navigator.clipboard.writeText(params.value);
    alert("Copied: " + params.value);
  };
  const HandleOnButtonClickClearFilter = (e) => {
    console.log(e);
    gridApi.getFilterInstance("SYMBOL").setModel(null); // replace 'yourColumnName' with your column name
    gridApi.onFilterChanged();
  };

  const getMaxValue = (CHG_IN_OI) => {
    let maxValue = null;
    let minValue = null;
    gridApi.forEachNode((node) => {
      if (maxValue === null || node.data[CHG_IN_OI] > maxValue) {
        maxValue = node.data[CHG_IN_OI];
      }
    });

    gridApi.forEachNode((node) => {
      if (minValue === null || node.data[CHG_IN_OI] < minValue) {
        minValue = node.data[CHG_IN_OI];
      }
    });

    alert("Max value / Min vAlue: " + maxValue + "/" + minValue);
  };

  const getRowHeight = (params) => {
    const isDetailRow = params.node.detail;
    if (!isDetailRow) {
      return undefined;
    }
    const detailPanelHeight = params.data.children.length * 50;
    return detailPanelHeight;
  };

  return (
    <Row>
      <Col className="ag-theme-alpine" style={{ height: 888, width: 2200 }}>
        {/* <div > */}
        <AgGridReact
          onGridReady={onGridReady}
          rowSelection="single"
          onSelectionChanged={onSelectionChanged}
          onCellDoubleClicked={onCellDoubleClicked}
          columnDefs={columnDefs}
          rowData={rowData}
          pagination={true}
          masterDetail={true}
          detailCellRenderer={(props) => <DetailsComponent {...props} />}
          detailRowHeight={getRowHeight}
          // keepDetailRows={true}
          // keepDetailRowsCount={5}
        ></AgGridReact>
        {/* </div> */}
      </Col>
      <Col>
        <Row>HELLO</Row>
        <Row>HELLO2 </Row>
      </Col>
    </Row>
  );
};

export default StockTable;
