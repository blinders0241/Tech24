import { Button, Card, Col, Container, Row } from "react-bootstrap";
import FFEditDBDetails from "./FFEditDBDetails";
import Accordion from "react-bootstrap/Accordion";
import { useEffect, useState } from "react";
import Placeholder from "react-bootstrap/Placeholder";

const FarFlixMovieDetailsPage = (props) => {
  const Directors_IMDB = props.data.Directors_IMDB;
  const [rowData, setRowData] = useState([]);
  const Plot_IMDB = props.data.Plot_IMDB;
  const Title_IMDB = props.data.Title_IMDB;
  const Year_IMDB = props.data.Year_IMDB;
  const ID = props.data.id;
  const FilePath = props.data.FilePath;
  const [trigger, setTrigger] = useState(0);

  // console.log(frequency);
  const allNotesapi = "http://127.0.0.1:8000/farFlix/";
  const preventDefault = (event) => {
    event.preventDefault();
  };
  useEffect(() => {
    let url = new URL(allNotesapi + "FarFlixFileDetails/");
    let params = { param1: props.data.MovieCode_IMDB };
    Object.keys(params).forEach((key) =>
      url.searchParams.append(key, params[key])
    );
    fetch(url)
      .then((result) => result.json())
      .then((rowData) => {
        setRowData(rowData);
        console.log("Do GE", rowData[0].FilePath);
        console.log(typeof rowData[0].FilePath);
      });
  }, [trigger]);

  // function convertRuntime(runtimeInMinutes) {
  //   if (isNaN(runtime)) {
  //     console.log(`Error: Unable to convert "${runtimeStr}" to a number.`);
  //     return null;
  //   }
  //   let runtimeStr = runtimeInMinutes.replace(/'/g, '"'); // Replace single quotes with double quotes
  //   let runtimeArr = JSON.parse(runtimeStr); // Parse the string as an array
  //   let runtime = parseInt(runtimeArr[0], 10); // Convert the first element to a number

  //   let hours = Math.floor(runtime / 60);
  //   let minutes = runtime % 60;
  //   return `${hours}h ${minutes}m`;
  // }
  function convertRuntime(runtimeInMinutes) {
    let runtimeArr;

    // Check if runtimeInMinutes is a string representation of a list
    if (
      typeof runtimeInMinutes === "string" &&
      runtimeInMinutes.startsWith("[") &&
      runtimeInMinutes.endsWith("]")
    ) {
      let runtimeStr = runtimeInMinutes.replace(/'/g, '"'); // Replace single quotes with double quotes
      try {
        runtimeArr = JSON.parse(runtimeStr); // Parse the string as an array
      } catch (e) {
        console.log(`Error: Unable to parse "${runtimeStr}" as JSON.`);
        return null;
      }
    } else if (Array.isArray(runtimeInMinutes)) {
      // If runtimeInMinutes is an actual list, use it directly
      runtimeArr = runtimeInMinutes;
    } else {
      console.log(
        `Error: "${runtimeInMinutes}" is not a list or a string representation of a list.`
      );
      return null;
    }

    let runtime = parseInt(runtimeArr[0], 10); // Convert the first element to a number

    if (isNaN(runtime)) {
      console.log(`Error: Unable to convert "${runtimeArr[0]}" to a number.`);
      return null;
    }

    let hours = Math.floor(runtime / 60);
    let minutes = runtime % 60;
    return `${hours}h ${minutes}m`;
  }
  // Usage
  let runtime = props.data.Runtime_IMDB; // Assuming getRunTIme is defined
  // console.log("Runtime for this Movie", runtime);
  let runtimeStr = convertRuntime(runtime);
  const handlethiButtonClick = (params) => {
    // console.log(params);
    navigator.clipboard.writeText(params);
    alert("FillePathCopied , Use Start + RUN / Launch vlc & paste: " + params);
  };
  return (
    <>
      <Container style={{ backgroundColor: "#D7DBDD", height: "300px" }}>
        <Row>
          <Col xs={6}>
            <Card style={{ width: "40rem" }}>
              <Card.Body>
                <Card.Title>
                  {Title_IMDB} &nbsp; {Year_IMDB}
                </Card.Title>
                <Card.Subtitle
                  className="mb-2 text-muted"
                  style={{
                    overflowWrap: "break-word",
                    whiteSpace: "normal",
                    userSelect: "text",
                  }}
                >
                  <b>RunTIme:</b> &nbsp;
                  {runtimeStr}&nbsp;&nbsp;
                  <b>Director:</b> &nbsp;
                  {Directors_IMDB}&nbsp;&nbsp;
                  <b>Plot:</b> &nbsp;
                  {Plot_IMDB}
                </Card.Subtitle>
                <Card.Text></Card.Text>
              </Card.Body>
            </Card>
          </Col>
          <Col>
            <Accordion>
              <Accordion.Item eventKey="0">
                <Accordion.Header>Update Movie Details</Accordion.Header>
                <Accordion.Body>
                  <FFEditDBDetails id={ID} filePath={FilePath} />
                </Accordion.Body>
              </Accordion.Item>
            </Accordion>
            <Placeholder.Button xs={12} aria-hidden="true">
              Admin Details
            </Placeholder.Button>
            <div>
              {rowData[0] && (
                <Container>
                  <Row>
                    <Button variant="secondary" size="sm">
                      diskInAction : <b>{rowData[0].Classified}</b> &nbsp;
                      sizeFile : <b>{rowData[0].FileSize}</b>
                    </Button>

                    <Button variant="secondary" size="sm">
                      sizeFile : {rowData[0].FilePath}
                    </Button>
                  </Row>
                  <Row>
                    <Button
                      onClick={() => {
                        handlethiButtonClick(rowData[0].FilePath);
                      }}
                    >
                      Play Movie
                    </Button>
                  </Row>
                </Container>
              )}
            </div>
          </Col>
        </Row>
      </Container>
    </>
  );
};

export default FarFlixMovieDetailsPage;
