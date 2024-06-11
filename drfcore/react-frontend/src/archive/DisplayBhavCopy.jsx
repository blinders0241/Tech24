import { useState } from "react";
import axios from "axios";
import StockTable from "../components/StockTable";

function DisplayBhavCopy() {
  const [stockName, setStockName] = useState("");
  const [timeFrame, setTimeFrame] = useState("");
  const [tableData, setTableData] = useState([]);
  const allNotesapi = "http://127.0.0.1:8000/api/";

  const preventDefault = (event) => {
    event.preventDefault();
  };

  const handleNameChange = (e) => {
    setStockName(e.target.value);
  };

  const handleChange = (e) => {
    setStockName(e.target.value);
  };

  const handleSelectionChange = (e) => {
    setTimeFrame(e.target.value);
  };

  const displayStockdetails = async (e) => {
    axios
      .get(allNotesapi + "displayBhavcopy/", {
        params: {
          value: stockName,
          timeFrame: timeFrame,
        },
      })
      .then((response) => {
        setTableData(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
      }}
    >
      <div class="container text-center">
        <div class="row">
          <div class="col-sm-8">
            {" "}
            <input
              type="text"
              value={stockName}
              onChange={handleNameChange}
            ></input>
            <button
              onClick={displayStockdetails}
              style={{
                height: "35px",
                width: "150px",
                backgroundColor: "#33AA2A",
                color: "#fff",
                cursor: "pointer",
                border: "None",
              }}
            >
              Get StockDetails
            </button>
          </div>
          <div class="col-sm-4">
            <select
              id={timeFrame}
              value={timeFrame}
              defaultValue="Daily"
              onChange={handleSelectionChange}
              class="form-control"
            >
              <option value="Daily">Daily</option>
              <option value="Weekly">Weekly</option>
              <option value="Monthly">Monthly</option>
            </select>
          </div>
        </div>
        <div class="container text-center">
          <div class="row">
            <div class="col-sm-2">
              <div class="card">
                <div class="card-body">
                  <h5 class="card-title">Card title</h5>
                  <h6 class="card-subtitle mb-2 text-muted">Card subtitle</h6>
                  <p class="card-text">
                    Some quick example text to build on the card title and make
                    up the bulk of the card's content.
                  </p>
                  <a href="#" class="card-link">
                    Card link
                  </a>
                  <a href="#" class="card-link">
                    Another link
                  </a>
                </div>
              </div>
            </div>
            <div class="col-sm-10">
              <StockTable data={tableData} />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default DisplayBhavCopy;
