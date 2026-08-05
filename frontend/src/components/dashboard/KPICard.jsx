import {
  Card,
  CardContent,
  Typography,
} from "@mui/material";

export default function KPICard({
  title,
  value,
}) {
  return (
    <Card elevation={3}>
      <CardContent>

        <Typography
          color="text.secondary"
        >
          {title}
        </Typography>

        <Typography
          variant="h3"
        >
          {value}
        </Typography>

      </CardContent>
    </Card>
  );
}