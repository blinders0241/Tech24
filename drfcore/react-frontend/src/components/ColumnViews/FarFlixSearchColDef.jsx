export const columndef_allmovies = [
  {
    headerName: "Movie Title",
    field: "Title_IMDB",
    filter: "agTextColumnFilter",
    filterParams: {
      buttons: ["apply", "reset"],
      closeOnApply: true,
    },
    floatingFilter: true,
    cellRenderer: "agGroupCellRenderer",
    width: 280,
  },
  {
    headerName: "Year",
    field: "Year_IMDB",
    filter: "agTextColumnFilter",
    width: 80,
    floatingFilter: true,
  },
  {
    headerName: "Language",
    field: "Language_IMDB",
    filter: "agTextColumnFilter",
    floatingFilter: true,
    width: 130,
  },

  {
    headerName: "Director",
    field: "Directors_IMDB",
    filter: "agTextColumnFilter",
    floatingFilter: true,
  },

  {
    headerName: "StarCast",
    field: "Cast_IMDB",
    filter: "agTextColumnFilter",
    floatingFilter: true,
    width: 380,
  },

  {
    headerName: "Rating",
    field: "Rating_IMDB",
    filter: "agTextColumnFilter",
    floatingFilter: true,
    width: 80,
  },
  {
    headerName: "Genres",
    field: "Genres_IMDB",
    width: 210,
    filter: "agTextColumnFilter",
    floatingFilter: true,
  },

];
