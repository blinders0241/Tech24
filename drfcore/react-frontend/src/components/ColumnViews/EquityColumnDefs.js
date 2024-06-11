import moment from "moment";

export const columndef_daily_allstocks = [
  {
    headerName: "SYMBOL",
    field: "SYMBOL",
    // checkboxSelection: true,
    filter: "agTextColumnFilter",
    floatingFilter: true,
    cellRenderer: "agGroupCellRenderer",
  },

  {
    headerName: "% Volume",
    field: "pVolume",
    width: 110,
    cellStyle: (params) =>
      params.value > 50 ? { color: "green" } : { color: "red" },
  },

  // {
  //   headerName: "%change",
  //   field: "pChange",
  //   width: 144,
  //   valueFormatter: (params) => `${params.value}%`,
  //   cellStyle: (params) => {
  //     const value = parseFloat(params.value);
  //     let color;
  //     if ((value >= 1) & (value <= 5)) {
  //       color = "lightgreen"; // for values 0-25
  //     } else if (value >= 5) {
  //       color = "green"; // for values 26-50
  //     } else if ((value > 0) & (value < 1)) {
  //       color = "orange"; // for values 51-75
  //     } else if ((value < 0) & (value > -1)) {
  //       color = "orange"; // for values 51-75
  //     } else {
  //       color = "red"; // for values 76-100
  //     }
  //     return { backgroundColor: color, fontWeight: "bold" };
  //   },
  // },

  {
    headerName: "Timestamp",
    field: "TIMESTAMP",
    width: 150,
    valueGetter: (params) => {
      if (params.data.TIMESTAMP) {
        // console.log("Received TimeStamp", params.data);
        let receivedDate = params.data.TIMESTAMP.split(" ")[0];
        // console.log("KUCH receivedDate", receivedDate);
        let dateParts = receivedDate.split("-");
        return new Date(dateParts[0], dateParts[1] - 1, dateParts[2]);
      } else {
        return "";
      }
    },
    valueFormatter: (params) => {
      return moment(params.value).format("ddd, DD-MMM-YY");
    },
  },

  {
    headerName: "Listed",
    field: "classifiedLists",
    width: 180,
    cellStyle: { fontSize: "small" },
  },

  {
    headerName: "ClosingPrice",
    field: "CLOSE",
    width: 180,
    cellStyle: { fontSize: "medium" },
    valueFormatter: (params) => {
      return params.value && typeof params.value === "number"
        ? "₹" + params.value.toLocaleString()
        : "";
    },
  },
];

export const columnDefsForWeek = [
  {
    headerName: "SYMBOL",
    field: "SYMBOL",
    // checkboxSelection: true,
    filter: "agTextColumnFilter",
    floatingFilter: true,
    cellRenderer: "agGroupCellRenderer",
  },

  {
    headerName: "% Volume",
    field: "pVolume",
    width: 110,
    cellStyle: (params) =>
      params.value > 50 ? { color: "green" } : { color: "red" },
  },

  {
    headerName: "Volume",
    field: "VOLUME",
    width: 110,
    valueFormatter: (params) => params.value.toLocaleString(),
  },

  {
    headerName: "OpenInterest",
    field: "OPEN_INT",
    width: 122,
    valueFormatter: (params) => (params.value / 1000000).toFixed(2) + "M",
  },

  {
    headerName: "OIChange",
    field: "CHG_IN_OI",
    width: 144,
    valueFormatter: (params) => (params.value / 1000000).toFixed(2) + "M",
    // cellStyle: (params) => console.log(typeof params.value),
  },

  {
    headerName: "%change",
    field: "pChange",
    width: 144,
    valueFormatter: (params) => `${params.value}%`,
    cellStyle: (params) => {
      const value = parseFloat(params.value);
      let color;
      if ((value >= 1) & (value <= 5)) {
        color = "lightgreen"; // for values 0-25
      } else if (value >= 5) {
        color = "green"; // for values 26-50
      } else if ((value > 0) & (value < 1)) {
        color = "orange"; // for values 51-75
      } else if ((value < 0) & (value > -1)) {
        color = "orange"; // for values 51-75
      } else {
        color = "red"; // for values 76-100
      }
      return { backgroundColor: color, fontWeight: "bold" };
    },
  },

  {
    headerName: "ClosingPrice",
    field: "CLOSE",
    width: 180,
    cellStyle: { fontSize: "medium" },
    valueFormatter: (params) => {
      return params.value && typeof params.value === "number"
        ? "₹" + params.value.toLocaleString()
        : "";
    },
  },

  {
    headerName: "Week",
    field: "Week",
    width: 110,
    cellStyle: { fontSize: "medium" },
    valueFormatter: (params) => {
      if (params.value) {
        const date = new Date(params.value);
        const day = date.getDate();
        const monthIndex = date.getMonth();
        const year = date.getFullYear().toString().substr(-2);

        const monthNames = [
          "Jan",
          "Feb",
          "Mar",
          "Apr",
          "May",
          "Jun",
          "Jul",
          "Aug",
          "Sep",
          "Oct",
          "Nov",
          "Dec",
        ];

        return `${day}-${monthNames[monthIndex]}-${year}`;
      }
      return null;
    },
  },
];

export const columnDefsForMonth = [
  {
    headerName: "SYMBOL",
    field: "SYMBOL",
    // checkboxSelection: true,
    filter: "agTextColumnFilter",
    floatingFilter: true,
    cellRenderer: "agGroupCellRenderer",
  },

  {
    headerName: "% Volume",
    field: "pVolume",
    width: 110,
    cellStyle: (params) =>
      params.value > 50 ? { color: "green" } : { color: "red" },
  },

  {
    headerName: "Volume",
    field: "VOLUME",
    width: 110,
    valueFormatter: (params) => params.value.toLocaleString(),
  },

  {
    headerName: "OpenInterest",
    field: "OPEN_INT",
    width: 122,
    valueFormatter: (params) => (params.value / 1000000).toFixed(2) + "M",
  },

  {
    headerName: "OIChange",
    field: "CHG_IN_OI",
    width: 144,
    valueFormatter: (params) => (params.value / 1000000).toFixed(2) + "M",
    // cellStyle: (params) => console.log(typeof params.value),
  },

  {
    headerName: "%change",
    field: "pChange",
    width: 144,
    valueFormatter: (params) => `${params.value}%`,
    cellStyle: (params) => {
      const value = parseFloat(params.value);
      let color;
      if ((value >= 1) & (value <= 5)) {
        color = "lightgreen"; // for values 0-25
      } else if (value >= 5) {
        color = "green"; // for values 26-50
      } else if ((value > 0) & (value < 1)) {
        color = "orange"; // for values 51-75
      } else if ((value < 0) & (value > -1)) {
        color = "orange"; // for values 51-75
      } else {
        color = "red"; // for values 76-100
      }
      return { backgroundColor: color, fontWeight: "bold" };
    },
  },

  {
    headerName: "ClosingPrice",
    field: "CLOSE",
    width: 180,
    cellStyle: { fontSize: "medium" },
    valueFormatter: (params) => {
      return params.value && typeof params.value === "number"
        ? "₹" + params.value.toLocaleString()
        : "";
    },
  },

  {
    headerName: "Month",
    field: "Month",
    width: 110,
    cellStyle: { fontSize: "medium" },
    valueFormatter: (params) => {
      if (params.value) {
        const date = new Date(params.value);
        const day = date.getDate();
        const monthIndex = date.getMonth();
        const year = date.getFullYear().toString().substr(-2);

        const monthNames = [
          "Jan",
          "Feb",
          "Mar",
          "Apr",
          "May",
          "Jun",
          "Jul",
          "Aug",
          "Sep",
          "Oct",
          "Nov",
          "Dec",
        ];

        return `${day}-${monthNames[monthIndex]}-${year}`;
      }
      return null;
    },
  },
];

// These Headers will be considered for the details Renderer
export const columnDefsFrequencyDaily = [
  {
    headerName: "Timestamp",
    field: "TIMESTAMP",
    width: 100,
    valueFormatter: (params) => {
      if (params.value) {
        const date = new Date(params.value);
        const day = date.getDate();
        const monthIndex = date.getMonth();
        const year = date.getFullYear().toString().substr(-2);

        const monthNames = [
          "Jan",
          "Feb",
          "Mar",
          "Apr",
          "May",
          "Jun",
          "Jul",
          "Aug",
          "Sep",
          "Oct",
          "Nov",
          "Dec",
        ];

        return `${day}-${monthNames[monthIndex]}-${year}`;
      }
      return null;
    },
  },
  {
    headerName: "ClosingPrice",
    field: "CLOSE",
    width: 110,
    valueFormatter: (params) => {
      return params.value && typeof params.value === "number"
        ? "₹" + params.value.toLocaleString()
        : "";
    },
  },
  {
    headerName: "Signal",
    field: "Signal",
    width: 130,
    cellStyle: (params) => {
      const value = params.value;
      let color;
      if (value == "Shorts BuildUp") {
        color = "red"; // for values 0-25
      } else if (value == "Long BuildUp") {
        color = "green"; // for values 26-50
      } else if (value == "Long Liquidation") {
        color = "orange"; // for values 51-75
      } else if (value == "Shorts Covering") {
        color = "lightgreen"; // for values 51-75
      } else {
        color = "red"; // for values 76-100
      }
      return { backgroundColor: color, fontWeight: "bold" };
    },
  },

  {
    headerName: "%change",
    field: "pChange",
    width: 144,
    valueFormatter: (params) => `${params.value}%`,
    cellStyle: (params) => {
      const value = parseFloat(params.value);
      let color;
      if ((value >= 1) & (value <= 5)) {
        color = "lightgreen"; // for values 0-25
      } else if (value >= 5) {
        color = "green"; // for values 26-50
      } else if ((value > 0) & (value < 1)) {
        color = "orange"; // for values 51-75
      } else if ((value < 0) & (value > -1)) {
        color = "orange"; // for values 51-75
      } else {
        color = "red"; // for values 76-100
      }
      return { backgroundColor: color, fontWeight: "bold" };
    },
  },

  {
    headerName: "% COI",
    field: "pCOI",
    width: 144,
    valueFormatter: (params) => `${params.value}%`,
    cellStyle: (params) => {
      const value = parseFloat(params.value);
      let color;
      if ((value >= 1) & (value <= 5)) {
        color = "lightgreen"; // for values 0-25
      } else if (value >= 5) {
        color = "green"; // for values 26-50
      } else if ((value > 0) & (value < 1)) {
        color = "orange"; // for values 51-75
      } else if ((value < 0) & (value > -1)) {
        color = "orange"; // for values 51-75
      } else {
        color = "red"; // for values 76-100
      }
      return { backgroundColor: color, fontWeight: "bold" };
    },
  },

  {
    headerName: "Volume",
    field: "VOLUME",
    width: 100,
    valueFormatter: (params) => params.value,
  },

  {
    headerName: "OpenIntrest",
    field: "OPEN_INT",
    width: 110,
    valueFormatter: (params) => (params.value / 1000000).toFixed(2) + "M",
  },

  {
    headerName: "OIChange",
    field: "CHG_IN_OI",
    width: 100,
    valueFormatter: (params) => (params.value / 1000000).toFixed(2) + "M",
  },

  {
    headerName: "OPEN",
    field: "OPEN",
    width: 110,
    valueFormatter: (params) => {
      return params.value && typeof params.value === "number"
        ? "₹" + params.value.toLocaleString()
        : "";
    },
  },
  {
    headerName: "HIGH",
    field: "HIGH",
    width: 110,
    valueFormatter: (params) => {
      return params.value && typeof params.value === "number"
        ? "₹" + params.value.toLocaleString()
        : "";
    },
  },
  {
    headerName: "LOW",
    field: "LOW",
    width: 110,
    valueFormatter: (params) => {
      return params.value && typeof params.value === "number"
        ? "₹" + params.value.toLocaleString()
        : "";
    },
  },
];

export const columnDefsFrequencyWeekly = [
  {
    headerName: "Week",
    field: "Week",
    width: 110,
    cellStyle: { fontSize: "medium" },
    valueFormatter: (params) => {
      if (params.value) {
        const date = new Date(params.value);
        const day = date.getDate();
        const monthIndex = date.getMonth();
        const year = date.getFullYear().toString().substr(-2);

        const monthNames = [
          "Jan",
          "Feb",
          "Mar",
          "Apr",
          "May",
          "Jun",
          "Jul",
          "Aug",
          "Sep",
          "Oct",
          "Nov",
          "Dec",
        ];

        return `${day}-${monthNames[monthIndex]}-${year}`;
      }
      return null;
    },
  },

  {
    headerName: "ClosingPrice",
    field: "CLOSE",
    width: 110,
    valueFormatter: (params) => {
      return params.value && typeof params.value === "number"
        ? "₹" + params.value.toLocaleString()
        : "";
    },
  },
  {
    headerName: "Signal",
    field: "Signal",
    width: 130,
    valueFormatter: (params) => params.value.toLocaleString(),
    cellStyle: (params) => {
      const value = params.value;
      let color;
      if (value == "Shorts BuildUp") {
        color = "red"; // for values 0-25
      } else if (value == "Long BuildUp") {
        color = "green"; // for values 26-50
      } else if (value == "Long Liquidation") {
        color = "orange"; // for values 51-75
      } else if (value == "Shorts Covering") {
        color = "lightgreen"; // for values 51-75
      } else {
        color = "red"; // for values 76-100
      }
      return { backgroundColor: color, fontWeight: "bold" };
    },
  },

  {
    headerName: "%change",
    field: "pChange",
    width: 144,
    valueFormatter: (params) => `${params.value}%`,
    cellStyle: (params) => {
      const value = parseFloat(params.value);
      let color;
      if ((value >= 1) & (value <= 5)) {
        color = "lightgreen"; // for values 0-25
      } else if (value >= 5) {
        color = "green"; // for values 26-50
      } else if ((value > 0) & (value < 1)) {
        color = "orange"; // for values 51-75
      } else if ((value < 0) & (value > -1)) {
        color = "orange"; // for values 51-75
      } else {
        color = "red"; // for values 76-100
      }
      return { backgroundColor: color, fontWeight: "bold" };
    },
  },

  {
    headerName: "% COI",
    field: "pCOI",
    width: 144,
    valueFormatter: (params) => `${params.value}%`,
    cellStyle: (params) => {
      const value = parseFloat(params.value);
      let color;
      if ((value >= 1) & (value <= 5)) {
        color = "lightgreen"; // for values 0-25
      } else if (value >= 5) {
        color = "green"; // for values 26-50
      } else if ((value > 0) & (value < 1)) {
        color = "orange"; // for values 51-75
      } else if ((value < 0) & (value > -1)) {
        color = "orange"; // for values 51-75
      } else {
        color = "red"; // for values 76-100
      }
      return { backgroundColor: color, fontWeight: "bold" };
    },
  },

  {
    headerName: "Volume",
    field: "VOLUME",
    width: 100,
    valueFormatter: (params) => params.value.toLocaleString(),
  },

  {
    headerName: "OpenIntrest",
    field: "OPEN_INT",
    width: 110,
    valueFormatter: (params) => (params.value / 1000000).toFixed(2) + "M",
  },

  {
    headerName: "OIChange",
    field: "CHG_IN_OI",
    width: 100,
    valueFormatter: (params) => (params.value / 1000000).toFixed(2) + "M",
  },

  {
    headerName: "OPEN",
    field: "OPEN",
    width: 110,
    valueFormatter: (params) => {
      return params.value && typeof params.value === "number"
        ? "₹" + params.value.toLocaleString()
        : "";
    },
  },
  {
    headerName: "HIGH",
    field: "HIGH",
    width: 110,
    valueFormatter: (params) => {
      return params.value && typeof params.value === "number"
        ? "₹" + params.value.toLocaleString()
        : "";
    },
  },
  {
    headerName: "LOW",
    field: "LOW",
    width: 110,
    valueFormatter: (params) => {
      return params.value && typeof params.value === "number"
        ? "₹" + params.value.toLocaleString()
        : "";
    },
  },
];

export const columnDefsFrequencyMonthly = [
  {
    headerName: "Month",
    field: "Month",
    width: 110,
    cellStyle: { fontSize: "medium" },
    valueFormatter: (params) => {
      if (params.value) {
        const date = new Date(params.value);
        const day = date.getDate();
        const monthIndex = date.getMonth();
        const year = date.getFullYear().toString().substr(-2);

        const monthNames = [
          "Jan",
          "Feb",
          "Mar",
          "Apr",
          "May",
          "Jun",
          "Jul",
          "Aug",
          "Sep",
          "Oct",
          "Nov",
          "Dec",
        ];

        return `${day}-${monthNames[monthIndex]}-${year}`;
      }
      return null;
    },
  },
  {
    headerName: "ClosingPrice",
    field: "CLOSE",
    width: 110,
    valueFormatter: (params) => {
      return params.value && typeof params.value === "number"
        ? "₹" + params.value.toLocaleString()
        : "";
    },
  },
  {
    headerName: "Signal",
    field: "Signal",
    width: 130,
    valueFormatter: (params) => params.value.toLocaleString(),
    cellStyle: (params) => {
      const value = params.value;
      let color;
      if (value == "Shorts BuildUp") {
        color = "red"; // for values 0-25
      } else if (value == "Long BuildUp") {
        color = "green"; // for values 26-50
      } else if (value == "Long Liquidation") {
        color = "orange"; // for values 51-75
      } else if (value == "Shorts Covering") {
        color = "lightgreen"; // for values 51-75
      } else {
        color = "red"; // for values 76-100
      }
      return { backgroundColor: color, fontWeight: "bold" };
    },
  },

  {
    headerName: "%change",
    field: "pChange",
    width: 144,
    valueFormatter: (params) => `${params.value}%`,
    cellStyle: (params) => {
      const value = parseFloat(params.value);
      let color;
      if ((value >= 1) & (value <= 5)) {
        color = "lightgreen"; // for values 0-25
      } else if (value >= 5) {
        color = "green"; // for values 26-50
      } else if ((value > 0) & (value < 1)) {
        color = "orange"; // for values 51-75
      } else if ((value < 0) & (value > -1)) {
        color = "orange"; // for values 51-75
      } else {
        color = "red"; // for values 76-100
      }
      return { backgroundColor: color, fontWeight: "bold" };
    },
  },

  {
    headerName: "% COI",
    field: "pCOI",
    width: 144,
    valueFormatter: (params) => `${params.value}%`,
    cellStyle: (params) => {
      const value = parseFloat(params.value);
      let color;
      if ((value >= 1) & (value <= 5)) {
        color = "lightgreen"; // for values 0-25
      } else if (value >= 5) {
        color = "green"; // for values 26-50
      } else if ((value > 0) & (value < 1)) {
        color = "orange"; // for values 51-75
      } else if ((value < 0) & (value > -1)) {
        color = "orange"; // for values 51-75
      } else {
        color = "red"; // for values 76-100
      }
      return { backgroundColor: color, fontWeight: "bold" };
    },
  },

  {
    headerName: "Volume",
    field: "VOLUME",
    width: 100,
    valueFormatter: (params) => params.value.toLocaleString(),
  },

  {
    headerName: "OpenIntrest",
    field: "OPEN_INT",
    width: 110,
    valueFormatter: (params) => (params.value / 1000000).toFixed(2) + "M",
  },

  {
    headerName: "OIChange",
    field: "CHG_IN_OI",
    width: 100,
    valueFormatter: (params) => (params.value / 1000000).toFixed(2) + "M",
  },

  {
    headerName: "OPEN",
    field: "OPEN",
    width: 110,
    valueFormatter: (params) => {
      return params.value && typeof params.value === "number"
        ? "₹" + params.value.toLocaleString()
        : "";
    },
  },
  {
    headerName: "HIGH",
    field: "HIGH",
    width: 110,
    valueFormatter: (params) => {
      return params.value && typeof params.value === "number"
        ? "₹" + params.value.toLocaleString()
        : "";
    },
  },
  {
    headerName: "LOW",
    field: "LOW",
    width: 110,
    valueFormatter: (params) => {
      return params.value && typeof params.value === "number"
        ? "₹" + params.value.toLocaleString()
        : "";
    },
  },
];
