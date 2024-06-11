import { useEffect, useState, useRef } from "react";
import axios from "axios";
import { Container, Row, Col, Card, Button } from "react-bootstrap";

const HeatMap = () => {
  const allNotesapi = "http://127.0.0.1:8000/api/";
  const [selectedOption, setSelectedOption] = useState("nifty");
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [toggle, setToggle] = useState(false);

  const options = [
    "auto",
    "banks",
    "energy",
    "finance",
    "fmcg",
    "it",
    "metals",
    "pharma",
    "nifty",
    "fno",
  ];
  const index = useRef(0);

  useEffect(() => {
    fetchData();
    const interval = setInterval(() => {
      index.current = (index.current + 1) % options.length;
      setSelectedOption(options[index.current]);
    }, 90000);
    return () => clearInterval(interval);
  }, [selectedOption]);

  const fetchData = async () => {
    setLoading(true);
    try {
      const response = await axios.get(`${allNotesapi}heatMap/`, {
        params: {
          index: selectedOption,
        },
      });
      const sortedData = response.data.sort(
        (a, b) => b["% Change"] - a["% Change"]
      );
      setData(sortedData);
    } catch (error) {
      console.error(error);
    }
    setLoading(false);
  };

  const handleChange = (event) => {
    setSelectedOption(event.target.value);
  };

  const handleToggle = () => {
    setToggle(!toggle);
    if (!toggle) {
      alert("Thanks");
    }
  };

  return (
    <Container fluid>
      {loading ? <div>Loading...</div> : null}
      <select value={selectedOption} onChange={handleChange}>
        {options.map((option) => (
          <option key={option} value={option}>
            {option.charAt(0).toUpperCase() + option.slice(1)}
          </option>
        ))}
      </select>
      <Button onClick={handleToggle}>Toggle</Button>
      <Row>
        {data.map((item, index) => {
          let cardColor;
          if (item["% Change"] > 0) {
            cardColor = "success";
          } else if (item["% Change"] < 0) {
            cardColor = "danger";
          } else {
            cardColor = "secondary";
          }

          return (
            <Col md={4} lg={3} xl={2} key={index}>
              <Card
                bg={cardColor}
                text="white"
                style={{ height: "110px", marginBottom: "10px" }}
                className="text-center"
              >
                <Card.Header>
                  {item.Symbol} ₹
                  {item["Last Traded Value"].toLocaleString("en-IN")}
                </Card.Header>
                <Card.Body>
                  <Card.Title>{item["% Change"]}</Card.Title>
                </Card.Body>
              </Card>
            </Col>
          );
        })}
      </Row>
    </Container>
  );
};

export default HeatMap;
