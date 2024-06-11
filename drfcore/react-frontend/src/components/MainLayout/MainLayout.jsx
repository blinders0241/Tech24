import Editor from "../MarkDownEditor/editor";
import Preview from "../MarkDownPreview/preview";
import { Container, Row, Col } from "react-bootstrap";
import TitleBar from "../TitleBar/TitleBar";
import { useMarkdown } from "../../providers/markdown-provider";
import { useState } from "react";

const MainLayout = ({ ExternalText }) => {
  const [markdownEditorArea, setMarkdown] = useMarkdown();
  const [words, setWords] = useState(0);
  const [chars, setChars] = useState(0);
  const [markdown] = useMarkdown();

  console.log(ExternalText);

  const getWordsCount = (str) => {
    return str.match(/(\w+)/g).length;
  };

  const getCharsCount = (str) => {
    return str.length;
  };

  const updateMarkdownEditingArea = (event) => {
    const value = event.target.value;
    setMarkdown(value);
    setWords(getWordsCount(value));
    setChars(getCharsCount(value));

    // setMarkdown(text);
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
    <>
      <Container fluid>
        <Row>
          <Col>
            <TitleBar
              title="Notes Summary"
              aside={`${words} Words ${chars} Characters`}
            />
          </Col>
          <Col>
            <button onClick={downloadFile}>Download File</button>
          </Col>
        </Row>
        <Row>
          <Col>
            <textarea
              style={{ height: "800px", width: "100%" }}
              value={markdownEditorArea}
              onChange={updateMarkdownEditingArea}
            ></textarea>
          </Col>
          <Col>
            <Preview />
          </Col>
        </Row>
      </Container>
    </>
  );
};
export default MainLayout;
