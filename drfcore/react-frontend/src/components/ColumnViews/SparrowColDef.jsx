export const columndef_SparrowLive = [
  {
    headerName: "Time",
    field: "Time",
    width: 110,
  },

  {
    headerName: "Max Pain",
    field: "MaxPain",
    width: 110,
  },
  {
    headerName: "PCR",
    field: "PCR",
    filter: "agTextColumnFilter",
    width: 80,
  },
  {
    headerName: "PCR_TV",
    field: "PCR_TradedVol",
    width: 110,
  },

  {
    headerName: "PE Cum_COI",
    field: "total_COI_PE",
    width: 130,
    valueFormatter: (params) => {
      return params.value && typeof params.value === "number"
        ? params.value.toLocaleString()
        : "";
    },
  },

  {
    headerName: "CE Cum_COI",
    field: "total_COI_CE",
    width: 130,
    valueFormatter: (params) => {
      return params.value && typeof params.value === "number"
        ? params.value.toLocaleString()
        : "";
    },
  },

  {
    headerName: "Live",
    field: "underlying",
    width: 130,
  },

  {
    headerName: "Put decay",
    field: "put_decay",
    width: 130,
  },

  {
    headerName: "Call decay",
    field: "call_decay",
    width: 130,
  },

  {
    headerName: "Expiry Date",
    field: "ExpiryDate",
    width: 130,
  },
];

export const columndef_OptionChainNIFTY = [
  {
    headerName: "StrikePrice",
    field: "strikePrice",
    width: 110,
  },

  {
    headerName: "Option Identifier",
    field: "identifier",
    width: 110,
  },
  {
    headerName: "open Interest",
    field: "openInterest",
    filter: "agTextColumnFilter",
    width: 80,
  },
  {
    headerName: "changeinOpenInterest",
    field: "changeinOpenInterest",
    width: 110,
  },

  {
    headerName: "% changeinOpenInterest",
    field: "pchangeinOpenInterest",
    width: 130,
    valueFormatter: (params) => {
      return params.value && typeof params.value === "number"
        ? params.value.toLocaleString()
        : "";
    },
  },

  {
    headerName: "totalSellQuantity",
    field: "totalSellQuantity",
    width: 130,
    valueFormatter: (params) => {
      return params.value && typeof params.value === "number"
        ? params.value.toLocaleString()
        : "";
    },
  },

  {
    headerName: "bidQty",
    field: "bidQty",
    width: 130,
  },

  {
    headerName: "bidprice",
    field: "bidprice",
    width: 130,
  },

  {
    headerName: "askQty",
    field: "askQty",
    width: 130,
  },

  {
    headerName: "askPrice",
    field: "askPrice",
    width: 130,
  },
];
