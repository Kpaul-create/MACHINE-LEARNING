import { IFAQ } from "@/types";
import { siteDetails } from "./siteDetails";

export const faqs: IFAQ[] = [
    {
        question: `How does ${siteDetails.siteName} work?`,
        answer: 'Simply send us a photo of your garment, and our AI pipeline creates stunning editorial-grade imagery. Our human editors then refine every detail to ensure perfection.',
    },
    {
        question: 'What types of products can you work with?',
        answer: 'We specialize in fashion and apparel, from clothing and accessories to footwear. Our AI can handle any garment type and create diverse model representations.',
    },
    {
        question: 'How long does the process take?',
        answer: 'We deliver your transformed imagery within 24 hours, or it\'s on us. Most projects are completed even faster depending on complexity and volume.'
    },
    {
        question: 'Do I need to provide models or styling?',
        answer: 'Not at all! Our AI creates diverse models and styling automatically. No need for physical models, studios, or extensive styling teams.',
    },
    {
        question: 'What makes your imagery different from other AI services?',
        answer: 'We combine cutting-edge AI with human editors who perfect every pixel. This hybrid approach ensures editorial-grade quality that stands out from purely AI-generated content.',
    },
    {
        question: 'Can you match my brand\'s aesthetic?',
        answer: 'Absolutely! We work with you to understand your brand\'s visual identity and create imagery that perfectly matches your aesthetic and target audience.',
    },
    {
        question: 'What file formats do you deliver?',
        answer: 'We provide high-resolution images in all standard formats (JPEG, PNG, TIFF) optimized for web, print, and social media platforms.',
    }
];