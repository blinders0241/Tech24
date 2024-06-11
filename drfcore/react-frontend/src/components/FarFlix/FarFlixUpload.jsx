import { useEffect, useState } from "react";
import {
  Button,
  Alert,
  Spinner,
  Container,
  Row,
  Col,
  Table,
} from "react-bootstrap";
import axios from "axios";
function FarFlixUpload() {
  const [uploading, setUploading] = useState(false);
  const [dataTable, setDataTable] = useState([]);
  const [totalFileSize, setTotalFileSize] = useState(0);
  const [diskName, setDiskName] = useState("");
  const [lastRowId, setLastRowId] = useState(0);
  const [keepUploadedFile, setKeepUploadedFile] = useState("loading...");
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState("No File Selected");
  const [success, setSuccess] = useState("");
  const EquityapiDB = "http://127.0.0.1:8000/farFlix/";
  const handleDrop = (event) => {
    event.preventDefault();
    const file = event.dataTransfer.files[0];
    setFile(file);
  };

  const preventDefault = (event) => {
    event.preventDefault();
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("csvFile", file);
    setKeepUploadedFile(file.name);
    // setStatus("Saving in progress...");
    setUploading(true);
    try {
      const response = await axios.post(
        EquityapiDB + "FarFlixUpload/",
        formData
      );
      setStatus(response.data["result"]);
      setUploading(false);
      setSuccess(true);
      setFile(null);
    } catch (error) {
      console.log(error);
    }
  };

  const handleClearDB = async (e) => {
    if (
      window.confirm("Are you sure : you want to CLEAN Entire DB for Equity?")
    )
      try {
        const response = await axios.get(EquityapiDB + "deleteEquity/");
        setStatus(response);
        // handle success
        console.log(response);
      } catch (error) {
        console.log(error);
      }
  };
  const getLatestDBDate = async () => {
    try {
      const response = await axios.get(EquityapiDB + "FF_FetchDetailsFromDB/");
      const data = response.data;
      setDataTable(data.slice(0, 20)); // Limit to top 30 rows

      // Calculate the total file size
      const totalSize = data.reduce((total, row) => total + row.FileSize, 0);
      setTotalFileSize(totalSize);
      const DiskName = data[data.length - 1].Classified;
      setDiskName(DiskName);
      console.log(diskName);

      // Get the ID of the last row
      if (data.length > 0) {
        setLastRowId(data[data.length - 1].id);
      }
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    getLatestDBDate();
  }, []);

  return (
    <>
      <Container>
        <Row>
          <Col md={6}>
            <h1>Upload Movies Data</h1>
            {/* <input type="file" onChange={handleUpload} multiple /> */}
            <form
              onSubmit={handleSubmit}
              style={{
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
              }}
            >
              <input
                class="custom-file-input"
                type="file"
                accept=".csv"
                onChange={(e) => setFile(e.target.files[0])}
              />

              <div
                onDrop={handleDrop}
                onDragOver={preventDefault}
                style={{
                  border: "3px dashed #f08080",
                  borderRadius: "10px",
                  padding: "30px",
                  textAlign: "center",
                  cursor: "pointer",
                  width: "100%",
                  marginBottom: "15px",
                  backgroundColor: "#fafad2",
                  color: "#696969",
                  fontSize: "20px",
                  fontWeight: "bold",
                  fontFamily: "'Courier New', Courier, monospace",
                  transition: "all 0.3s ease-out",
                  ":hover": {
                    transform: "scale(1.05)",
                    backgroundColor: "#f08080",
                    color: "#fff",
                  },
                }}
              >
                {file ? (
                  <div>Selected File: {file.name} </div>
                ) : (
                  <h1>Feed ME Please Last Feed {file}</h1>
                )}
              </div>
              <button
                type="submit"
                style={{
                  height: "35px",
                  width: "150px",
                  backgroundColor: "#33AA2A",
                  color: "#fff",
                  opacity: file ? 1 : 0.6,
                  cursor: file ? "pointer" : "not-allowed",
                  border: "None",
                  marginBottom: "0.5rem",
                }}
                disabled={!file}
              >
                Upload CSV
              </button>
            </form>
            {uploading && <Spinner animation="border" />}
            {
              <Alert
                variant="success"
                className="text-center"
                style={{ fontSize: "20px", fontWeight: "bold" }}
              >
                File upload Status: {status}
                <h3 style={{ color: "#17a2b8" }}>
                  FileName: {keepUploadedFile}
                </h3>
              </Alert>
            }
            <Button variant="danger" onClick={handleClearDB}>
              Clear DB
            </Button>
          </Col>
          <Col md={6}>
            {/* You can add your additional content here */}
            {/* <Button variant="danger" onClick={getLatestDBDate}>
              Get DB Info
            </Button> */}

            {/* Telegram content */}

            <Container>
              {" "}
              <Row>
                <Col>
                  <Button variant="danger" onClick={getLatestDBDate}>
                    Get DB Info
                  </Button>
                  <Alert variant="info">
                    Total File Size: {totalFileSize} GB <br />
                    {/* Number of Movies: {lastRowId} <br /> */}
                    <h3>{diskName}</h3>
                  </Alert>
                  <Table striped bordered hover>
                    <thead>
                      <tr>
                        <th>ID</th>
                        {/* <th>File Path</th> */}
                        <th>Movie Name</th>
                        <th>File Size</th>
                        {/* <th>File Type</th> */}
                        {/* Add more headers if needed */}
                      </tr>
                    </thead>
                    <tbody>
                      {dataTable.map((item, index) => (
                        <tr key={index}>
                          <td>{item.id}</td>
                          {/* <td>{item.FilePath}</td> */}
                          <td>{item.movieName_Disk}</td>
                          <td>{item.FileSize}</td>
                          {/* <td>{item.FileType}</td> */}
                          {/* Add more data cells if needed */}
                        </tr>
                      ))}
                    </tbody>
                  </Table>
                </Col>
              </Row>
            </Container>
            {/* Twitter content */}

            <h2>Top 10 Blogs</h2>
            {/* Blog content */}
          </Col>
        </Row>
      </Container>
    </>
  );
}

export default FarFlixUpload;
