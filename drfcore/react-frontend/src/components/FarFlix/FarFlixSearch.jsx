import { useEffect, useState } from "react";
import Container from "react-bootstrap/Container";
import Button from "react-bootstrap/Button";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import axios from "axios";
import { columndef_allmovies } from "../ColumnViews/FarFlixSearchColDef/";
import FarFlixTable from "./FarFlixTable";
import { Typography } from "@mui/material";
import { Link } from "react-router-dom";

function FarFlixSearch() {
  const [fetcher, setFetcher] = useState(false);
  const [frequency, setFrequency] = useState("D");
  const [rowData, setRowData] = useState([]);
  const [trigger, setTrigger] = useState(0);

  // console.log(frequency);
  const allNotesapi = "http://127.0.0.1:8000/farFlix/";
  const preventDefault = (event) => {
    event.preventDefault();
  };
  useEffect(() => {
    let url = new URL(allNotesapi + "FarFlixSearch/");
    let params = { param1: frequency };

    Object.keys(params).forEach((key) =>
      url.searchParams.append(key, params[key])
    );

    fetch(url)
      .then((result) => result.json())
      .then((rowData) => {
        setRowData(rowData);
      });
  }, [trigger]);

  const handleButtonSortYear = (e) => {
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

  return (
    <>
      <Container fluid>
        <Row>
          <Col>

            <Typography
                variant="h6"
                component={Link}
                to="/youTube"
                sx={{
                  color: "white",
                  textDecoration: "none",
                  letterSpacing: "1px",
                  marginLeft: "10px",
                  marginRight: "10px",
                  // fontStyle: "oblique",
                  fontSize: "18px", // text size
                }}
              >
                HeatMap
              </Typography>
            <Button variant="outline-danger">Danger</Button>{" "}
            <Button variant="outline-light">Light</Button>{" "}
            <Button variant="outline-dark">Dark</Button>
          </Col>
        </Row>
        <Row>
          <Col>
            <FarFlixTable columnDefs={columndef_allmovies} rowData={rowData} />
          </Col>
        </Row>
      </Container>
    </>
  );
}

export default FarFlixSearch;
