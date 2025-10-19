import { IMenuItem, ISocials } from "@/types";

export const footerDetails: {
    subheading: string;
    quickLinks: IMenuItem[];
    email: string;
    telephone: string;
    socials: ISocials;
} = {
    subheading: "Transforming fashion imagery with AI-powered creativity and human precision.",
    quickLinks: [
        {
            text: "How It Works",
            url: "#features"
        },
        {
            text: "Pricing",
            url: "#pricing"
        },
        {
            text: "Testimonials",
            url: "#testimonials"
        }
    ],
    email: 'hello@finaura.ai',
    telephone: '+91 9123993358',
    socials: {
        // github: 'https://github.com',
        // x: 'https://twitter.com/x',
        twitter: 'https://twitter.com/finaura_ai',
        facebook: 'https://facebook.com/finaura.ai',
        // youtube: 'https://youtube.com',
        linkedin: 'https://www.linkedin.com/company/finaura-ai-studio',
        // threads: 'https://www.threads.net',
        instagram: 'https://www.instagram.com/finaura.ai',
    }
}