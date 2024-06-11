import { useEffect, useState } from "react";
import StockTable from "./StockTable";
import Container from "react-bootstrap/Container";
import Button from "react-bootstrap/Button";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import axios from "axios";
// import axios from "axios";
import {
  columndef_daily_allstocks,
  columnDefsForWeek,
  columnDefsForMonth,
} from "../../ColumnViews/EquityColumnDefs/";

function DisplayEquity() {
  // const [clearFilter, setClearFilter] = useState(false);
  const [fetcher, setFetcher] = useState(false);
  const [frequency, setFrequency] = useState("D");
  const [rowData, setRowData] = useState([]);
  const [trigger, setTrigger] = useState(0);

  // console.log(frequency);
  const allNotesapi = "http://127.0.0.1:8000/equity/";
  const preventDefault = (event) => {
    event.preventDefault();
  };
  useEffect(() => {
    let url = new URL(allNotesapi + "displayEquityetails/");
    let params = { param1: frequency };

    Object.keys(params).forEach((key) =>
      url.searchParams.append(key, params[key])
    );
    // let url = new URL();
    fetch(url)
      .then((result) => result.json())
      .then((rowData) => {
        setRowData(rowData);
        // console.log("Do GE", rowData);
      });
  }, [trigger]);

  const handleButtonClickFetchDaily = (e) => {
    setFetcher(true);
    setFrequency(e.target.value);
    setTrigger(trigger + 1);
  };

  const handleButtonClickFetchWeekly = (e) => {
    setFrequency(e.target.value);
    setTrigger(trigger + 1);
  };
  const handleButtonClickFetchMonthly = (e) => {
    setFrequency(e.target.value);
    setTrigger(trigger + 1);
  };

  let columnDefs;
  switch (frequency) {
    case "D":
      columnDefs = columndef_daily_allstocks;
      break;
    case "W":
      columnDefs = columnDefsForWeek;
      break;
    case "M":
      columnDefs = columnDefsForMonth;
      break;
    default:
      columnDefs = columnDefsProfileDisplayAllFNO; // replace with your default column definitions
  }

  return (
    <>
      <Container fluid>
        <Row>
          <Col>
            <Button
              variant="outline-primary"
              id="Daily"
              value="D"
              onClick={handleButtonClickFetchDaily}
            >
              Daily
            </Button>
            <Button
              variant="outline-secondary"
              id="Weekly"
              value="W"
              onClick={handleButtonClickFetchWeekly}
            >
              Weekly
            </Button>
            <Button
              variant="outline-success"
              id="Monthly"
              value="M"
              onClick={handleButtonClickFetchMonthly}
            >
              Monthly
            </Button>
            {/* <Button variant="outline-warning" onClick={clearAllFilters}> */}
            {/* </Button>{" "} */}
            <Button variant="outline-danger">Danger</Button>{" "}
            <Button variant="outline-light">Light</Button>{" "}
            <Button variant="outline-dark">Dark</Button>
          </Col>
        </Row>
        <Row>
          <Col>
            <StockTable columnDefs={columnDefs} rowData={rowData} />
          </Col>
        </Row>
      </Container>
    </>
  );
}

export default DisplayEquity;
