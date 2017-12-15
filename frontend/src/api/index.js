/**
 * Created by Владислав on 15.12.2017.
 */
/**
 * Created by Владислав on 11.12.2017.
 */
// src/auth/index.js
// URL and endpoint constants
const API_URL = 'http://localhost:8000/api/'
const PLACES = API_URL + 'places/'

export default {
  place_list (context) {
    context.axios.get(PLACES, {
      withCredentials: true
    }).then((response) => {
      return response.data
    })
  }
}
