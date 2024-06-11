export const columndef_allmovies = [
  {
    headerName: "Movie Title",
    field: "Title_IMDB",
    filter: "agTextColumnFilter",
    floatingFilter: true,
    cellRenderer: "agGroupCellRenderer",
  },
  {
    headerName: "Year of Release",
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
    width: 310,
  },

  {
    headerName: "IMDB Rating",
    field: "Rating_IMDB",
    filter: "agTextColumnFilter",
    floatingFilter: true,
  },
  {
    headerName: "Genres",
    field: "Genres_IMDB",
    width: 210,
    filter: "agTextColumnFilter",
    floatingFilter: true,
  },

  // {
  //   headerName: "File Size",
  //   field: "FileSize",
  // },

  // {
  //   headerName: "Play Video",
  //   field: "FilePath",
  //   width: 144,
  //   cellRendererFramework: (params) => {
  //     return (
  //       <a href={params.value} target="_blank" rel="noopener noreferrer">
  //         Play Video
  //       </a>
  //     );
  //   },
  // },
];
