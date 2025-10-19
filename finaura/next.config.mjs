/** @type {import('next').NextConfig} */
const nextConfig = {
  webpack: (config) => {
    // Disable Webpack filesystem cache to avoid ENOSPC errors in constrained environments
    config.cache = false;
    return config;
  },
};

export default nextConfig;
