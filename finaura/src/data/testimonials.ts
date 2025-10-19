import { ITestimonial } from "@/types";
import { siteDetails } from "./siteDetails";

export const testimonials: ITestimonial[] = [
    {
        name: 'Sarah Chen',
        role: 'Creative Director at StyleCo',
        message: `${siteDetails.siteName} has revolutionized our product photography. What used to take weeks of planning and thousands in costs now happens in 24 hours. The quality is absolutely stunning.`,
        avatar: '/images/testimonial-1.webp',
    },
    {
        name: 'Marcus Rodriguez',
        role: 'E-commerce Manager at TrendBrand',
        message: `The AI-generated models and styling are incredibly diverse and realistic. Our conversion rates have increased by 40% since we started using ${siteDetails.siteName} for our product listings.`,
        avatar: '/images/testimonial-2.webp',
    },
    {
        name: 'Emma Thompson',
        role: 'Marketing Director at Fashion Forward',
        message: `Working with ${siteDetails.siteName} has been a game-changer. No more expensive photo shoots, model bookings, or studio rentals. Just pure, editorial-grade imagery that our customers love.`,
        avatar: '/images/testimonial-3.webp',
    },
];