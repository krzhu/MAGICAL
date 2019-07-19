/****************************************************************************

COPYRIGHT NOTICE:

  The source code in this directory is provided free of
  charge to anyone who wants it.  It is in the public domain
  and therefore may be used by anybody for any purpose.  It
  is provided "AS IS" with no warranty of any kind
  whatsoever.  For further details see the README files in
  the wnlib parent directory.

AUTHOR:

  Will Naylor

****************************************************************************/
#ifndef wnstkH
#define wnstkH

#include "wncons.h"
#include "wnsll.h"
#include "wnmem.h"



typedef struct wn_stack_struct
{
  wn_sll top;
  wn_memgp group;
} *wn_stack;

typedef wn_sll wn_stackmark;


extern ptr wn_stacktop();



#define wn_push(_s,_e)        wn_push_routine(_s,(ptr)(_e))



#endif
