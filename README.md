# Coupon API Documentation

## Overview
This API allows users to manage discount coupons. It includes endpoints for creating, updating, deactivating, and deleting coupons.

## Base URL
```
http://127.0.0.1:8000/api/v1/coupons/
```

---

## 1. Create a Coupon (POST)

**Endpoint:**
```
POST /api/v1/coupons/
```

**Request Body (JSON):**
```json
{
  "code": "SAVE20",
  "discount_percentage": 20.0,
  "expiry_date": "2025-12-31",
  "is_active": true,
  "min_order_value": 100.00
}
```

**Expected Response:**
```
201 Created
```
```json
{
  "id": 1,
  "code": "SAVE20",
  "discount_percentage": 20.0,
  "expiry_date": "2025-12-31",
  "is_active": true,
  "min_order_value": 100.00
}
```

---

## 2. Update a Coupon (PUT/PATCH)

**Endpoint:**
```
PUT /api/v1/coupons/{id}/
PATCH /api/v1/coupons/{id}/
```

**Request Body (JSON):**
```json
{
  "discount_percentage": 25.0,
  "expiry_date": "2025-12-31"
}
```

**Expected Response:**
```
200 OK
```
```json
{
  "id": 1,
  "code": "SAVE20",
  "discount_percentage": 25.0,
  "expiry_date": "2025-12-31",
  "is_active": true,
  "min_order_value": 100.00
}
```

---

## 3. Deactivate a Coupon (POST)

**Endpoint:**
```
POST /api/v1/coupons/{id}/deactivate/
```

**Expected Response:**
```
200 OK
```
```json
{
  "message": "Coupon deactivated"
}
```

---

## 4. Delete a Coupon (DELETE)

**Endpoint:**
```
DELETE /api/v1/coupons/{id}/
```

**Expected Response:**
```
204 No Content
```

---

## 5. Filtering Coupons

### Get Active Coupons
```
GET /api/v1/coupons/?status=active
```

### Get Expired Coupons
```
GET /api/v1/coupons/?status=expired
```

---

## Postman Collection Export
- The Postman collection containing all requests can be found in `Coupon_API_Collection.json`.
- Import this file into Postman to quickly test the API.

---

## Submission Instructions
1. Save all Postman requests in a **Postman Collection**.
2. Export the collection as a JSON file (`Coupon_API_Collection.json`).
3. Upload the JSON file and this README to GitHub.
4. Submit the GitHub repository link.

---

## Notes
- Ensure `expiry_date` is **not in the past** when creating or updating a coupon.
- Only active coupons can be deactivated using the `deactivate/` endpoint.
- Coupons are filtered using the `status` query parameter (`active` or `expired`).
