import React, { useState, useEffect } from "react";
import axios from "axios";
import { Col, Container, Row } from "react-bootstrap";

const FFEditDBDetails = ({ id, filePath }) => {
  console.log("Recived", id);
  const [movieCode_IMDB, setMovieCode_IMDB] = useState("");
  const [year_IMDB, setYear_IMDB] = useState("");
  const [title_IMDB, setTitle_IMDB] = useState("");

  const EquityapiDB = "http://127.0.0.1:8000/farFlix/";
  // Fetch the movie details using the id when the component mounts

  const handleSubmit = (event) => {
    event.preventDefault();
    axios
      .post(EquityapiDB + "FF_FetchEditDetailsTODB/", {
        id: id,
        movieCode_IMDB: movieCode_IMDB,
        Year_IMDB: year_IMDB,
        Title_IMDB: title_IMDB,
      })
      .then((response) => {
        alert(response.data.message);
      })
      .catch((error) => {
        if (error.response) {
          alert(error.response.data.error);
        } else if (error.request) {
          alert("No response received");
        } else {
          alert("Error", error.message);
        }
      });
  };

  const handleDelete = () => {
    axios
      .post(EquityapiDB + "FF_DeleteMoviebyID/", { id: id })
      .then((response) => {
        alert(response.data.message);
      })
      .catch((error) => {
        if (error.response) {
          alert(error.response.data.error);
        } else if (error.request) {
          alert("No response received");
        } else {
          alert("Error", error.message);
        }
      });
  };

  return (
    <>
      <Row>
        <form onSubmit={handleSubmit}>
          <Row>
            <label>
              MovieCode IMDB &nbsp;
              <input
                type="text"
                value={movieCode_IMDB}
                onChange={(e) => setMovieCode_IMDB(e.target.value)}
              />
            </label>
            <label>
              Year IMDB:
              <input
                type="text"
                value={year_IMDB}
                onChange={(e) => setYear_IMDB(e.target.value)}
              />
            </label>
            <label>
              Title(Imdb):
              <input
                type="text"
                value={title_IMDB}
                onChange={(e) => setTitle_IMDB(e.target.value)}
              />
            </label>{" "}
          </Row>
          <Row>
            <Col>
              <label>
                File Path:
                <span>{filePath}</span>
              </label>
              <input type="submit" value="Submit" />
            </Col>{" "}
          </Row>
        </form>

        <button type="button" onClick={handleDelete}>
          Delete this Item
        </button>
      </Row>
    </>
  );
};

export default FFEditDBDetails;
