import { z } from 'zod';

export const MathInputSchema = z.object({ a: z.number(), b: z.number() });