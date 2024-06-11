import { useState } from "react";
import TitleBar from "../TitleBar/TitleBar";
import "./editor.css";
import { Container, Row, Col } from "react-bootstrap";
import { styled } from "@mui/system";

const PreviewDiv = styled("div")({
  color: "black",
  backgroundColor: "white",
  marginTop: "20px",
  marginLeft: "1px",
  fontSize: "16px",
  fontFamily: "Cambria",
  textAlign: "left",
  padding: "5px",
});

const Editor = () => {
  const getWordsCount = (str) => {
    return str.match(/(\w+)/g).length;
  };

  const getCharsCount = (str) => {
    return str.length;
  };

  const downloadFile = () => {
    const link = document.createElement("a");
    const file = new Blob([markdown], { type: "text/plain" });
    link.href = URL.createObjectURL(file);
    link.download = "Untitled.md";
    link.click();
    URL.revokeObjectURL(link.href);
  };

  return (
    <Container fluid>
      <Row>
        <Col xl={6}>
          <button onClick={downloadFile}>Download File</button>
        </Col>
      </Row>
      <Row></Row>
      <Row>
        <Col></Col>
      </Row>
    </Container>
  );
};

export default Editor;
