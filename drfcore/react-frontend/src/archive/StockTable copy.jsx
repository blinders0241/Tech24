import React from "react";
import { useTable } from "react-table";
import moment from "moment"; // import moment.js

import "../App.css";

function StockTable({ data }) {
  // const data = JSON.parse(receiveddata);
  const formatDate = (date) => {
    // use the format method with the desired pattern
    return moment(date).format("ddd, DDMMMYY");
  };
  const columns = React.useMemo(
    () => [
      // {
      //   Header: "ID",
      //   accessor: "id",
      // },
      {
        Header: "Symbol",
        accessor: "SYMBOL",
        // a custom filter function that matches the input value with the symbol
        Filter: ({ column: { filterValue, setFilter } }) => (
          <input
            value={filterValue || ""}
            onChange={(e) => setFilter(e.target.value)}
            placeholder="Search symbol..."
          />
        ),
      },
      {
        Header: "Open",
        accessor: "OPEN",
      },
      {
        Header: "High",
        accessor: "HIGH",
      },
      {
        Header: "Low",
        accessor: "LOW",
      },
      {
        Header: "Close",
        accessor: "CLOSE",
      },
      {
        Header: "Volume",
        accessor: "VOLUME",
      },
      {
        Header: "OpenInt",
        accessor: "OPEN_INT",
      },
      {
        Header: "OIChange",
        accessor: "CHG_IN_OI",
      },
      {
        Header: "Timestamp",
        accessor: "TIMESTAMP",
        // use the Cell prop to format the date
        Cell: ({ value }) => formatDate(value),
        sortType: (a, b) => {
          var a1 = new Date(a).getTime();
          var b1 = new Date(b).getTime();
          if (a1 < b1) return 1;
          else if (a1 > b1) return -1;
          else return 0;
        },
      },
    ],
    []
  );

  const { getTableProps, getTableBodyProps, headerGroups, rows, prepareRow } =
    useTable({ columns, data });

  return (
    <table {...getTableProps()}>
      <thead>
        {headerGroups.map((headerGroup) => (
          <tr {...headerGroup.getHeaderGroupProps()}>
            {headerGroup.headers.map((column) => (
              <th {...column.getHeaderProps()}>{column.render("Header")}</th>
            ))}
          </tr>
        ))}
      </thead>
      <tbody {...getTableBodyProps()}>
        {rows.map((row) => {
          prepareRow(row);
          return (
            <tr {...row.getRowProps()}>
              {row.cells.map((cell) => (
                <td {...cell.getCellProps()}>{cell.render("Cell")}</td>
              ))}
            </tr>
          );
        })}
      </tbody>
    </table>
  );
}

export default StockTable;
