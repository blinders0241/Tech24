import React from "react";
import { DataTable } from "primereact/datatable";
import { Column } from "primereact/column";

function StockTable({ data }) {
  return (
    <>
      <DataTable value={data}>
        <Column field="SYMBOL" header="Symbol" />
        <Column field="OPEN" header="Open" />
        <Column field="HIGH" header="High" />
        <Column field="LOW" header="Low" />
        <Column field="CLOSE" header="Close" />
        <Column field="VOLUME" header="Volume" sortable />
        <Column field="OPEN_INT" header="OpenInt" sortable />
        <Column field="CHG_IN_OI" header="Change in OpenInt" />
        <Column field="TIMESTAMP" header="Timestamp" />
      </DataTable>
    </>
  );
}

export default StockTable;
