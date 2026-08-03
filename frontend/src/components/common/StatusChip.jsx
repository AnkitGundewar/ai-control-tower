import Chip from "@mui/material/Chip";

export default function StatusChip({ status }) {
  let color = "default";

  switch (status) {
    case "Delivered":
      color = "success";
      break;

    case "In Transit":
      color = "info";
      break;

    case "At Risk":
      color = "warning";
      break;

    case "Delayed":
      color = "error";
      break;
  }

  return (
    <Chip
      label={status}
      color={color}
      size="small"
      variant="filled"
    />
  );
}