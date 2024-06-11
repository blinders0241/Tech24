import React, { useEffect, useState } from "react";
import axios from "axios";
import axiosRetry from "axios-retry";
import DataGrid from "./DataGrid";

import Button from "react-bootstrap/esm/Button";
import { Accordion, ButtonGroup, Col, Container, Row } from "react-bootstrap";
import DataGrid2 from "./DataGrid2";
import {
  columndef_SparrowLive,
  columndef_OptionChainNIFTY,
} from "../ColumnViews/SparrowColDef/";
import DataGrid3 from "./DataGrid3";

// Configure axios to automatically retry failed requests 3 times
axiosRetry(axios, { retries: 3 });

function SparrowLive() {
  const [dataN, setDataN] = useState([]);
  const [dataB, setDataB] = useState([]);
  const [cetop10OIstrikeprice, setCEtop10OIstrikeprice] = useState([]);
  const [petop10OIstrikeprice, setPEtop10OIstrikeprice] = useState([]);

  const [isLoading, setIsLoading] = useState(true);
  const [trigger, setTrigger] = useState("NIFTY");
  const [index, setIndex] = useState("NIFTY");
  const [expiry, setExpiry] = useState("M");
  const [flag, setFlag] = useState("Column1");

  const sparrowEndPoint = "http://127.0.0.1:8000/sparrow/";
  let SetRunningTime = 16;
  useEffect(() => {
    const fetchData = async () => {
      const currentHour = new Date().getHours();
      if (currentHour < SetRunningTime) {
        try {
          const response = await axios.get(sparrowEndPoint + "sparrowHome/", {
            params: {
              // triggerType: trigger,
              inDexName: index, // Use trigger as the parameter
              expiry: expiry, // Use trigger as the parameter
            },
          });
          // console.log(response);
          const data = response.data[0];
          const data2 = response.data[1];
          const data3 = response.data[2];

          console.log("Printing Option Chain Data ############");
          console.log(trigger);

          if (index === "NIFTY") {
            setDataN(data);
            setFlag("column1");
          } else if (index === "BANKNIFTY") {
            setDataB(data);
            setFlag("column1");
          } else if (index === "handleCallStrikersOINIFTY") {
            // console.log("Main Ghus gaya Hoon");
            setCEtop10OIstrikeprice(data2);
            setFlag("column2");
          } else if (index === "handlePutStrikersOINIFTY") {
            // setDataB((prevData) => [...prevData, ...data]);
            setPEtop10OIstrikeprice(data3);
            setFlag("column2");
          }

          setIsLoading(false);
        } catch (error) {
          console.error("Error fetching data:", error);
        }
      }
    };

    // setData(result);
    fetchData();
    const intervalId = setInterval(fetchData, 3 * 60 * 1000);
    return () => clearInterval(intervalId);
  }, [trigger, expiry, index]);

  const handleButtonClickFetchDaily = () => {
    setIndex("NIFTY");
  };

  const handleButtonClickFetchBankNifty = (e) => {
    setIndex(e.target.value);
  };

  const handleButtonClickSetWeeklyExpiry = (e) => {
    setExpiry(e.target.textContent);
    // console.log(e);
  };

  const handleButtonClickSetMonthlyExpiry = (e) => {
    setExpiry(e.target.textContent);
    // console.log(e);
  };

  const handleCallStrikersOINIFTY = (e) => {
    setIndex("handleCallStrikersOINIFTY");
  };
  const handlePutStrikersOINIFTY = (e) => {
    setIndex("handlePutStrikersOINIFTY");
  };
  const handleCallStrikersOIBANKNIFTY = (e) => {
    setIndex(e.target.value);
  };
  const handlePutStrikersOIBANKNIFTY = (e) => {
    setIndex(e.target.value);
  };

  let columnDefs;
  switch (flag) {
    case "column1":
      columnDefs = columndef_SparrowLive;
      break;
    case "column2":
      columnDefs = columndef_OptionChainNIFTY;
      break;
    case "column3":
      columnDefs = columndef_OptionChainNIFTY;
      break;
    default:
      columnDefs = columndef_SparrowLive; // replace with your default column definitions
  }

  return (
    <Container fluid>
      <Row className="justify-content-md-center">
        <Col xs={2}>
          <ButtonGroup aria-label="Basic example">
            <Button
              variant="secondary"
              onClick={handleButtonClickSetWeeklyExpiry}
            >
              W
            </Button>
            <Button
              variant="primary"
              value="NIFTY"
              onClick={handleButtonClickFetchDaily}
            >
              Nifty
            </Button>
            <Button
              variant="secondary"
              onClick={handleButtonClickSetMonthlyExpiry}
            >
              M
            </Button>
          </ButtonGroup>
        </Col>

        <Col xs={2}>
          <Button
            variant="dark"
            value="NIFTY"
            onClick={handleCallStrikersOINIFTY}
          >
            N50CallStrikers OI{" "}
          </Button>
        </Col>
        <Col xs={2}>
          <Button
            variant="dark"
            value="NiftyPUT"
            onClick={handlePutStrikersOINIFTY}
          >
            N50PutStrikers OI{" "}
          </Button>
        </Col>
        <Col xs={2}>
          <ButtonGroup aria-label="Basic example">
            <Button
              variant="secondary"
              onClick={handleButtonClickSetWeeklyExpiry}
            >
              W
            </Button>
            <Button
              variant="primary"
              value="BANKNIFTY"
              onClick={handleButtonClickFetchBankNifty}
            >
              BANKNifty
            </Button>
            <Button
              variant="secondary"
              onClick={handleButtonClickSetMonthlyExpiry}
            >
              M
            </Button>
          </ButtonGroup>
        </Col>
        <Col xs={2}>
          <Button
            variant="dark"
            value="BANKNIFTYOptionChain"
            onClick={handleCallStrikersOIBANKNIFTY}
          >
            BNFCallStrikers OI{" "}
          </Button>
        </Col>
        <Col xs={2}>
          <Button
            variant="dark"
            value="BankNiftyPUT"
            onClick={handlePutStrikersOIBANKNIFTY}
          >
            BNFPutStrikers OI{" "}
          </Button>
        </Col>
      </Row>
      <Row className="justify-content-md-center">
        <Col xs={12}>
          <i>
            Active : {index}
            &nbsp;
            {expiry} Timing Set to Run till <i>{SetRunningTime}00</i> HRS
          </i>
        </Col>
      </Row>
      <Accordion defaultActiveKey={["0"]}>
        <Accordion.Item eventKey="0">
          <Accordion.Header>Nifty 50 {expiry}</Accordion.Header>
          <Accordion.Body>
            {isLoading ? (
              <p>Loading...</p>
            ) : (
              <DataGrid data={dataN} columnDefs={columnDefs} />
            )}
          </Accordion.Body>
        </Accordion.Item>
      </Accordion>
      {/* Second Frame on the Window */}
      <Accordion>
        <Accordion.Item eventKey="1">
          <Accordion.Header>Bank Nifty {expiry}</Accordion.Header>
          <Accordion.Body>
            {isLoading ? (
              <p>Loading...</p>
            ) : (
              <DataGrid data={dataB} columnDefs={columnDefs} />
            )}
          </Accordion.Body>
        </Accordion.Item>
      </Accordion>
      {/* Third Frame on the Window */}
      <Accordion>
        <Accordion.Item eventKey="2">
          <Accordion.Header>Nifty Call | StrikePrice to Buy</Accordion.Header>
          <Accordion.Body>
            {isLoading ? (
              <p>Loading...</p>
            ) : (
              <DataGrid2 data2={cetop10OIstrikeprice} columnDefs={columnDefs} />
            )}
          </Accordion.Body>
        </Accordion.Item>
      </Accordion>
      {/* Fourth Frame on the Window */}
      <Accordion>
        <Accordion.Item eventKey="2">
          <Accordion.Header>Nifty Put | StrikePrice to Buy</Accordion.Header>
          <Accordion.Body>
            {isLoading ? (
              <p>Loading...</p>
            ) : (
              <DataGrid3 data3={petop10OIstrikeprice} columnDefs={columnDefs} />
            )}
          </Accordion.Body>
        </Accordion.Item>
      </Accordion>

      {/* Fifth Frame on the Window */}
      <Accordion>
        <Accordion.Item eventKey="2">
          <Accordion.Header>
            BankNifty Call | StrikePrice to Buy
          </Accordion.Header>
          <Accordion.Body>
            {isLoading ? (
              <p>Loading...</p>
            ) : (
              <DataGrid2 data2={cetop10OIstrikeprice} columnDefs={columnDefs} />
            )}
          </Accordion.Body>
        </Accordion.Item>
      </Accordion>
      {/* Sizth Frame on the Window */}
      <Accordion>
        <Accordion.Item eventKey="2">
          <Accordion.Header>
            BankNifty Put | StrikePrice to Buy
          </Accordion.Header>
          <Accordion.Body>
            {isLoading ? (
              <p>Loading...</p>
            ) : (
              <DataGrid2 data2={cetop10OIstrikeprice} columnDefs={columnDefs} />
            )}
          </Accordion.Body>
        </Accordion.Item>
      </Accordion>
    </Container>
  );
}
export default SparrowLive;
