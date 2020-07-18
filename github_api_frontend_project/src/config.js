import config from 'react-global-configuration'



config.set({
    BackendHost: process.env.REACT_APP_BACKEND_HOST || "http://ec2-52-28-6-236.eu-central-1.compute.amazonaws.com:8000",
    AuthURL: process.env.REACT_APP_AUTH_URL || "http://ec2-52-28-6-236.eu-central-1.compute.amazonaws.com:8000/api/v1/authenticate",
})

