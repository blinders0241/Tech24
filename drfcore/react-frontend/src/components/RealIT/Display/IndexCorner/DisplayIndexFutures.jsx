import { useEffect, useState } from "react";
import StockTable from "../StockTable";
import Container from "react-bootstrap/Container";
import Button from "react-bootstrap/Button";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import axios from "axios";
// import {
//   columndef_daily_allstocks,
//   columnDefsForWeek,
//   columnDefsForMonth,
// } from "../../../ColumnViews/columnDefs/";

import { columndef_daily_allstocks } from "../../../ColumnViews/ColumnDefs/";
import { Typography } from "@mui/material";
import { Link } from "react-router-dom";

function DisplayIndexFutures() {
  const [fetcher, setFetcher] = useState(false);
  const [frequency, setFrequency] = useState("D");
  const [rowData, setRowData] = useState([]);
  const [trigger, setTrigger] = useState(0);

  const allNotesapi = "http://127.0.0.1:8000/api/";
  const preventDefault = (event) => {
    event.preventDefault();
  };
  useEffect(() => {
    let url = new URL(allNotesapi + "displayIndexdetails/");
    let params = { param1: frequency };

    Object.keys(params).forEach((key) =>
      url.searchParams.append(key, params[key])
    );
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
      columnDefs = columndef_daily_allstocks; // replace with your default column definitions
  }

  return (
    <>
      <Container fluid>
        <Row>
          <Col>
            <Typography
              variant="h6"
              component={Link}
              to="/IndexMeter"
              sx={{
                color: "green",
                textDecoration: "none",
                letterSpacing: "1px",
                marginLeft: "10px",
                marginRight: "10px",
                // fontStyle: "oblique",
                fontSize: "15px", // text size
              }}
            >
              IndexMeter
            </Typography>

            <Typography
              variant="h6"
              component={Link}
              to="/UploadIndexHistoricals"
              sx={{
                color: "blue",
                textDecoration: "none",
                letterSpacing: "1px",
                marginLeft: "10px",
                marginRight: "10px",
                // fontStyle: "oblique",
                fontSize: "15px", // text size
              }}
            >
              UploadIndexHistoricals
            </Typography>
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
          </Col>
        </Row>
        <Row>
          <Col>
            <StockTable columnDefs={columnDefs} rowData={rowData}></StockTable>
          </Col>
        </Row>
      </Container>
    </>
  );
}

export default DisplayIndexFutures;
