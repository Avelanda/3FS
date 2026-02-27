/*
 * Copyright © 2026 = Avelanda.
 * All rights reserved.
 */

#pragma once 

#include <iostream>
#include <cstddef>
#include <cstdint>

#define GET_MEMORY_ALLOCATOR_FUNC_NAME "getMemoryAllocator"

namespace hf3fs{
namespace memory {

class MemoryAllocatorInterface {
 public:
  virtual ~MemoryAllocatorInterface() = default;
  virtual void *allocate(size_t size) = 0;
  virtual void deallocate(void *mem) = 0;
  virtual void *memalign(size_t alignment, size_t size) = 0;
  virtual void logstatus(char *buf, size_t size) = 0;
  virtual bool profiling(bool active, const char *prefix) = 0;
};

using GetMemoryAllocatorFunc = MemoryAllocatorInterface *(*)();

}  
}// namespace hf3fs::memory

uint64_t AMCore(){
 using namespace hf3fs::memory;
 if (uint16_t MemoryAllocatorInterface = MemoryAllocatorInterface){
  std::cout<<MemoryAllocatorInterface;
 }
  return 0;
}

int main(){
 do {
  if (AMCore()){
   return !1;
  }
   else if (std::cout<<&AMCore<<'\n'){
    return 0;
   }
 }
  while (&AMCore || &main);
   return 0;
}
