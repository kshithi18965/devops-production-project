import http from "k6/http";
import { check, sleep } from "k6";

export const options = {
  stages: [
    { duration: "30s", target: 10 },  // ramp up to 10 virtual users
    { duration: "1m", target: 10 },   // hold steady at 10 for a minute
    { duration: "30s", target: 50 },  // ramp up to 50
    { duration: "1m", target: 50 },   // hold at 50
    { duration: "30s", target: 0 },   // ramp back down to 0
  ],
  thresholds: {
    http_req_duration: ["p(95)<500"], // 95% of requests should finish under 500ms
    http_req_failed: ["rate<0.01"],   // fewer than 1% of requests should fail
  },
};

const BASE_URL = "http://localhost:5000";

export default function () {
  // Hit the products list endpoint
  const listRes = http.get(`${BASE_URL}/products`);
  check(listRes, {
    "GET /products status is 200": (r) => r.status === 200,
  });

  // Hit a single product endpoint
  const detailRes = http.get(`${BASE_URL}/products/1`);
  check(detailRes, {
    "GET /products/1 status is 200": (r) => r.status === 200,
  });

  // Hit the health endpoint
  const healthRes = http.get(`${BASE_URL}/health`);
  check(healthRes, {
    "GET /health status is 200": (r) => r.status === 200,
  });

  sleep(1); // pause 1 second between each simulated user's requests
}
