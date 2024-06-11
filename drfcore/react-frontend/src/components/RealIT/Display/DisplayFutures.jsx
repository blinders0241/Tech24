import { useEffect, useState } from "react";
import StockTable from "./StockTable";
import Container from "react-bootstrap/Container";
import Button from "react-bootstrap/Button";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { FcHeatMap } from "react-icons/fc";

import axios from "axios";

import {
  columndef_daily_allstocks,
  columnDefsForWeek,
  columnDefsForMonth,
} from "../../ColumnViews/columnDefs/";
import { Alert, ButtonGroup } from "react-bootstrap";
import { Link } from "react-router-dom";
import { Typography } from "@mui/material";

function DisplayFutures() {
  const [isActive, setIsActive] = useState(false);
  const [frequency, setFrequency] = useState("D");
  const [rowData, setRowData] = useState([]);
  const [trigger, setTrigger] = useState(0);

  const allNotesapi = "http://127.0.0.1:8000/api/";
  const preventDefault = (event) => {
    event.preventDefault();
  };
  useEffect(() => {
    let url = new URL(allNotesapi + "displayStockdetails/");
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
    setFrequency(e.target.value);
    setTrigger(trigger + 1);
    setIsActive(true);
  };

  const handleButtonClickFetchWeekly = (e) => {
    setFrequency(e.target.value);
    setTrigger(trigger + 1);
    setIsActive(true);
  };
  const handleButtonClickFetchMonthly = (e) => {
    setFrequency(e.target.value);
    setTrigger(trigger + 1);
  };

  let columnDefs;
  let alert;
  switch (frequency) {
    case "D":
      columnDefs = columndef_daily_allstocks;
      alert = (
        <Alert variant="info">
          Showing Derivatives <b>Daily</b> data
        </Alert>
      );
      break;
    case "W":
      columnDefs = columnDefsForWeek;
      alert = (
        <Alert variant="info">
          Showing Derivatives <b>Weekly</b> data
        </Alert>
      );
      break;
    case "M":
      columnDefs = columnDefsForMonth;
      alert = (
        <Alert variant="info">
          Showing Derivatives <b>Monthly</b> data
        </Alert>
      );
      break;
    default:
      columnDefs = columnDefsProfileDisplayAllFNO; // replace with your default column definitions
  }

  return (
    <>
      <Container fluid>
        <Row>
          <Col>
            <Alert variant="light">
              <ButtonGroup size="sm">
                <Button onClick={handleButtonClickFetchDaily} value="D">
                  Daily
                </Button>
                <Button
                  variant="outline-secondary"
                  onClick={handleButtonClickFetchWeekly}
                  value="W"
                >
                  Week
                </Button>
                <Button onClick={handleButtonClickFetchMonthly} value="M">
                  Monthly
                </Button>
              </ButtonGroup>
              {/* WORKING AREA */}
              <Typography
                variant="h6"
                component={Link}
                to="/heatMap"
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
                HeatMap
              </Typography>
              <Typography
                variant="h6"
                component={Link}
                to="/sparrowHome"
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
                Sparrow
              </Typography>
              <Typography
                variant="h6"
                component={Link}
                to="/displayIndexdetails"
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
                IndexFutures
              </Typography>
              <Typography
                variant="h6"
                component={Link}
                to="/displayEquityetails"
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
                Equity
              </Typography>
              <Typography
                variant="h6"
                component={Link}
                to="/uploadData"
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
                Upload
              </Typography>
            </Alert>
          </Col>
          <Col>{alert}</Col>
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

export default DisplayFutures;
