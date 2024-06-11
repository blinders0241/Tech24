import { useState } from "react";
import { Col, Container, Row } from "react-bootstrap";
import Button from "react-bootstrap/Button";
import DOMPurify from "dompurify";

// import "../App.css";
const DetailsNotes = (props) => {
  const [rowData, setRowData] = useState([]);
  const [title, setTitle] = useState("");
  console.log(props);
  const highlightMatches = (text, match) => {
    const regex = new RegExp(`(${match})`, "gi");
    return text.replace(regex, "<strong>$1</strong>");
  };

  // const ExternalTextSender =(e) = {
  //   console.log();
  // }

  return (
    <>
      <Container fluid>
        <Row>
          <Col>
            <p
              style={{
                whiteSpace: "pre-wrap",
                fontFamily: "Calibri",
                fontSize: "large",
                color: "#21618C",
                marginRight: "5px",
                marginLeft: "5px",
                marginTop: "15px",
              }}
              dangerouslySetInnerHTML={{
                __html: highlightMatches(props.data.body, props.data.title),
              }}
            ></p>
          </Col>
        </Row>
      </Container>
    </>
  );
};
export default DetailsNotes;
