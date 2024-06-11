import { useEffect, useState } from "react";
import Button from "react-bootstrap/Button";
import ButtonGroup from "react-bootstrap/ButtonGroup";

import {
  columnDefsFrequencyDaily,
  columnDefsFrequencyWeekly,
  columnDefsFrequencyMonthly,
} from "../../ColumnViews/columnDefs/";

import moment from "moment";
import MyGridComponent from "./MyGridComponent";
const allNotesapi = "http://127.0.0.1:8000/api/";
// import "../App.css";
const DetailsComponent = (props) => {
  const [rowData, setRowData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let url = new URL(allNotesapi + "stockMasterDetail/");
    let params = { param1: props.data.freq, param2: props.data.SYMBOL };
    Object.keys(params).forEach((key) =>
      url.searchParams.append(key, params[key])
    );
    fetch(url) // replace 'your-api-url' with your API URL
      .then((result) => result.json())
      .then((rowData) => {
        setRowData(rowData);
        setLoading(false);
      });
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

  let columnDefs;
  switch (props.data.freq) {
    case "D":
      columnDefs = columnDefsFrequencyDaily;
      break;
    case "W":
      columnDefs = columnDefsFrequencyWeekly;
      break;
    case "M":
      columnDefs = columnDefsFrequencyMonthly;
      break;
    default:
      columnDefs = columndef_daily_allstocks; // replace with your default column definitions
  }

  if (loading) {
    return (
      <>
        {" "}
        <h1>Loading Data...</h1>
      </>
    );
  }
  return (
    <>
      <MyGridComponent
        onGridReady={onGridReady}
        columnDefs={columnDefs}
        rowData={rowData}
      />
    </>
  );
};
export default DetailsComponent;
