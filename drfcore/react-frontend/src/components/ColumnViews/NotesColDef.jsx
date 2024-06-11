import moment from "moment";
export const NotesColDef = [
  {
    headerName: "#Note",
    field: "id",
    width: 90,
    // cellRenderer: "agGroupCellRenderer",
  },

  {
    headerName: "Added on",
    field: "created",
    width: 150,
    valueFormatter: (params) => {
      return moment(params.value).format("ddd,DD-MMM-YY");
      // return moment(params.value).format("HH:mm | ddd,DD-MMM-YY");
    },
  },
  {
    headerName: "Notes Title",
    field: "title",
    cellStyle: { "font-weight": "bold", color: "blue" }, // Add this line
    width: 330,
    filter: "agTextColumnFilter",
    floatingFilter: true,
  },

  {
    headerName: "Tags ",
    field: "tags",
    filter: "agTextColumnFilter",
    floatingFilter: true,
    width: 190,
  },

  {
    headerName: "Classified",
    field: "reactions",
    filter: "agTextColumnFilter",
    floatingFilter: true,
    width: 140,
    cellStyle: function (params) {
      switch (params.value) {
        case "Deleted":
          return { color: "red" };
        case "Finance":
          return { color: "blue" };
        case "Personal":
          return { color: "green" };
        case "value4":
          return { color: "yellow" };
        case "Learnings":
          return { color: "purple" };
        case "Work":
          return { color: "orange" };
        default:
          return { color: "black" };
      }
    },
  },
  {
    headerName: "Last Updated",
    field: "updated",
    width: 160,
    valueFormatter: (params) => {
      return moment(params.value).format("HH:mm,DD-MMM-YY");
    },
  },
];
