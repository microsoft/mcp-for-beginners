import { z } from 'zod';

export interface Tool {
    name: string;
    inputSchema: any;
    rawSchema: any,
    callback: (args: z.infer<z.ZodTypeAny>) => Promise<{ content: { type: string; text: string }[] }>;
}